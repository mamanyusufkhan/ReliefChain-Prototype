from django.shortcuts import render
from .models import Blockchain

# Create your views here.
def ledger(request):
    blocks = Blockchain.objects.all()
    return render(request, 'ledger.html', {'blocks' : blocks})

def logbook(request):
    return render(request, 'blockchain/logbook.html')