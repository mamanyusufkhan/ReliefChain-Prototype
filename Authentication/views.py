from django.shortcuts import render,redirect
from .models import User, UserWallet
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def donor_login(request):
    if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password = password)
            if (user is not None) and (user.is_donor) == 1:
                login(request, user)
                return redirect('/donor/')
            else:
                messages.info(request, "Username or Password is incorrect.")

    return render(request , 'donor/donorLogin.html')

def donor_register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        username = request.POST.get('username')
        
        if form.is_valid():
            form.save()
            uobj = User.objects.get(username=username)   
            uobj.is_donor=1  
            uobj.is_admin=0 
            uobj.is_fundRaiser=0          
            uobj.save()
            wallet = UserWallet(user = uobj, amount = 0)
            wallet.save()
            return redirect('/auth/donorLogin/')
        
    context = {'form': form }
    return render(request , 'donor/donorReg.html',context)

def donor_logout(request):  
    logout(request)
    return redirect('/')

def fundRaiser_login(request):
    if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password = password)
            if (user is not None) and (user.is_fundRaiser) == 1:
                login(request, user)
                return redirect('/fundRaiser/')
            else:
                messages.info(request, "Username or Password is incorrect.")
    return render(request , 'fundRaiser/fundRaiserLogin.html')

def fundRaiser_register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        username = request.POST.get('username')
        
        if form.is_valid():
            form.save()
            uobj = User.objects.get(username=username)   
            uobj.is_donor=0  
            uobj.is_admin=0 
            uobj.is_fundRaiser=1         
            uobj.save()
            wallet = UserWallet(user = uobj, amount = 0)
            wallet.save()
            return redirect('/auth/fundRaiserLogin/')
        
    context = {'form': form }       
    return render(request , 'fundRaiser/fundRaiserReg.html',context)

def fundRaiser_logout(request):  
    logout(request)
    return redirect('/')

def admin_login(request):
    if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password = password)
            if (user is not None) and (user.is_admin) == 1:
                login(request, user)
                return redirect('/adminHome/')
            else:
                messages.info(request, "Username or Password is incorrect.")
    return render(request , 'admin/adminLogin.html')


def admin_register(request):
    return render(request , 'admin/adminReg.html')


def admin_logout(request):  
    logout(request)
    return redirect('/')