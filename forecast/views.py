from django.shortcuts import render
import requests
from geopy.geocoders import Nominatim

# Create your views here.
def getFloodData(request):

    if request.method =='POST':
        print("OK?")
        district = request.POST.get('district')
        start_date = request.POST.get('start-date')
        end_date = request.POST.get('end-date')

        # Define the API URL
        api_url = "https://flood-api.open-meteo.com/v1/flood"
        # start_date = "2023-11-01"
        # end_date = "2023-11-04"
        # district = 'Dhaka'
        # Create a geolocator object using Nominatim
        geolocator = Nominatim(user_agent="get_lat_long")
        location = district+', Bangladesh'
        # Use the geolocator to get the location information for Dhaka
        location = geolocator.geocode(location)

        # Extract the latitude and longitude from the location object
        latitude = location.latitude
        longitude = location.longitude
        print(latitude,longitude)
        # Define the query parameters
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "daily": "river_discharge,river_discharge_mean,river_discharge_median,river_discharge_max,river_discharge_min,river_discharge_p25,river_discharge_p75",
            "start_date": start_date,
            "end_date": end_date,
        }

        # Send a GET request to the API
        response = requests.get(api_url, params=params)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            size = len(data['daily']['river_discharge'])
            river_discharge = data['daily']['river_discharge']
            risk_index = []
            range = 0
            for water_level in river_discharge:
                if district=='Sylhet':
                    range = 4.8
                    if water_level  > 4.8:
                        risk_index.append('Flood')
                    else:
                        risk_index.append('No Flood')
                if district=='Rajshahi':
                    range = 50000
                    if water_level  > 50000:
                        risk_index.append('Flood')
                    else:
                        risk_index.append('No Flood')
                if district=='Chattogram':
                    range = 1000
                    if water_level  > 1000:
                        risk_index.append('Flood')
                    else:
                        risk_index.append('No Flood')
                if district=='Dhaka':
                    range = 12
                    if water_level  > 12:
                        risk_index.append('Flood')
                    else:
                        risk_index.append('No Flood')
            print("range",range)
            forecastData = {
                'dates' : data['daily']['time'],
                'river_discharge' : data['daily']['river_discharge'],
                'total_instances' : size,
                'start_date' : start_date,
                'end_date' : end_date,
                'district' : district,
                'risk_index' : risk_index,
                'range' : range
            }

            # Process the data as needed
            # For example, you can print the entire JSON response:
            return render(request, 'forecast.html', {'data' : forecastData})
        else:
            print("Error: Failed to retrieve data from the API.")
            print(f"Status Code: {response.status_code}")

def showData(request):
    return render(request, 'forecast_form.html')

