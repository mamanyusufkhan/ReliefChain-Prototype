from decimal import Decimal
from django.http import HttpResponse
from django.shortcuts import render, redirect
from Authentication.models import UserWallet
from events.models import Event, Escrow_Account
from donations.models import Donation
from datetime import datetime
from ledger.models import  Blockchain, BlockchainManager, hashGenerator

# Create your views here.
def home(request):
    
    events = Event.objects.all()
    new_list = []
    for event in events:
        raising_amount = float(event.Amount_to_be_raised)
        current_amount = float(event.current_amount)
        percentage = (current_amount/raising_amount) * 100

        new_list.append({
            'Event_ID': event.Event_ID,
            'Event_name': event.Event_name,
            'Event_details': event.Event_details,
            'FundRaiser': event.FundRaiser.username,
            'Category': event.Category,
            'Division': event.Division,
            'District': event.District,
            'Amount_to_be_raised': str(event.Amount_to_be_raised),
            'Minimum_amount_to_be_raised': str(event.Minimum_amount_to_be_raised),
            'Starts_at': event.Starts_at.strftime('%Y-%m-%d'),  # Format datetime as text
            'Ends_at': event.Ends_at.strftime('%Y-%m-%d'),      # Format datetime as text
            'Is_approved': event.Is_approved,
            'Current_amount':event.current_amount,   
            'Event_status': event.Event_status,
            'Percentage': percentage


    
        })

    userwallet = UserWallet.objects.get(user = request.user)
    context = {'wallet': userwallet, 'newlist': new_list}
    return render(request , 'homedonor.html', context)

def donate(request):

    if request.method == "POST":
        amount = request.POST["amount"]
        userwallet = UserWallet.objects.get(user = request.user)
        temp = float(userwallet.amount)
        temp += float(amount)
        userwallet.amount = Decimal(temp)
        userwallet.save()
        return redirect("/donor/")
    userwallet = UserWallet.objects.get(user = request.user)
    context = {'wallet': userwallet}
    return render(request , 'donateMoney.html', context)

def checkmodalvalue(request):
    if request.method == "POST":
        amount = request.POST["amount"]
        id = request.POST["eventId"]
        
        event = Event.objects.get(Event_ID = id)
        user = request.user

        userwallet = UserWallet.objects.get(user = user)
        escrowwallet = Escrow_Account.objects.get(event = event)
        fundraiserwallet = UserWallet.objects.get(user = event.FundRaiser)

        take_current_amount = float(event.current_amount)
        take_current_amount += float(amount)
        print(take_current_amount)
        event.current_amount = Decimal(take_current_amount)
        event.save()

        escrow_amount = float(escrowwallet.amount)
        print(escrow_amount)
        user_amount = float(amount)
        print(escrow_amount)
        escrow_amount += user_amount
        userwalletamount = float(userwallet.amount)
        userwalletamount -= user_amount
        userwallet.amount = Decimal(userwalletamount)
        userwallet.save()

        if take_current_amount >= float(event.Minimum_amount_to_be_raised):
            fundraiser_amount = float(fundraiserwallet.amount)
            fundraiser_amount += escrow_amount
            fundraiserwallet.amount = Decimal(fundraiser_amount)
            fundraiserwallet.save()
            escrow_amount = 0

        escrowwallet.amount = escrow_amount
        escrowwallet.save()

        donation = Donation(Event_Id = event, User_id = user, Amount = user_amount, DateTime = datetime.now())
        donation.save()

        data1 = {
            'Donation_ID': donation.Donation_id,
            'Event_Id' : event.Event_ID,
            'User_id' : user.id,
            'Event_Name': event.Event_name,
            'User_Name': user.username,
            'Amount' : user_amount,
            'DateTime' : datetime.now(),
            
        }
        
        blocks = Blockchain.objects.filter()
        print("1",blocks)
        print(blocks[len(blocks)-1])
        prev_block = blocks[len(blocks)-1]
        curr_hash = hashGenerator(str(data1['Donation_ID']))
        prev_hash = prev_block.hash
        b = Blockchain(data=data1, hash=curr_hash, prev_hash=prev_hash)
        b.save()
        


        
    return redirect("/donor/")