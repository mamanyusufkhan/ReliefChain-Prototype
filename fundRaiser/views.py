from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import date, datetime
from events.models import Event, Escrow_Account
from Authentication.models import UserWallet

# Create your views here.
def home(request):
    user = request.user
    if request.method == "POST":
        user = request.user
        event_name = request.POST["eventName"]
        event_details = request.POST["eventDescription"]
        fundraiser = request.user
        category = request.POST["eventCategory"]
        starts_at = datetime.now()
        starts_at = starts_at.date()
        ends_at = request.POST["eventEndsAt"]
        division = request.POST["eventDivision"]
        district = request.POST["eventDistrict"]
        amount_to_be_raised = request.POST["amountToBeRaised"]
        threshold_amount = request.POST["minimumAmount"]
        
    

        assigned_value = Event(Event_name = event_name, Event_details = event_details, FundRaiser = fundraiser, Category = category, Division = division, District = district, Amount_to_be_raised = amount_to_be_raised, Minimum_amount_to_be_raised = threshold_amount, Starts_at = starts_at, Ends_at = ends_at, Is_approved = True, Event_status = 'live')
        assigned_value.save()

        escrow_wallet = Escrow_Account(event = assigned_value, amount = 0)
        escrow_wallet.save()
        return redirect("/fundRaiser")

    wallet = UserWallet.objects.get(user = request.user)

    list_of_relief = Event.objects.filter(FundRaiser = user)
    event_data = []
    for event in list_of_relief:
        event_data.append({
            'Event_ID': event.Event_ID,
            'Event_name': event.Event_name,
            'Event_details': event.Event_details,
            'FundRaiser': event.FundRaiser.username,
            'Category': event.Category,
            'Division': event.Division,
            'District': event.District,
            'Amount_to_be_raised': str(event.Amount_to_be_raised),
            'Minimum_amount_to_be_raised': str(float(event.Minimum_amount_to_be_raised) - 1),
            'Starts_at': event.Starts_at.strftime('%Y-%m-%d'),  # Format datetime as text
            'Ends_at': event.Ends_at.strftime('%Y-%m-%d'),      # Format datetime as text
            'current_amount': event.current_amount,
            'Is_approved': event.Is_approved,
            'Event_status': event.Event_status,
        })
    context = {'relief': event_data, 'wallet': wallet}
    return render(request , 'homefr.html', context)

def events(request):
    return render(request, 'events.html')

def form(request):
    return render(request, 'form.html')


def donate(request):
    return render(request , 'donateMoney.html')