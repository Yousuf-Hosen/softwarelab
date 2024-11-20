from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from contracts.models import Contract
# Create your views here.


def register(request):
    if request.method == 'POST':
        #get form values
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        
        # check passwords are match
        if password == password2:
            #check username
            if User.objects.filter(username=username).exists():
                messages.error(request,'username is already taken')
                return redirect('register')
            else:
                #check email 
                if User.objects.filter(email=email).exists():
                    messages.error(request,'email is already exists')
                    return redirect('register')
                else:
                    user=User.objects.create_user(username=username,password=password,email=email,
                                                  first_name=first_name,last_name=last_name)
                    user.save()
                    messages.success(request,'you are now register and you can log in')
                    return redirect('login')       
        else:
            messages.error(request,'Password does not match')
        return redirect('register')
    else:  
      return render(request,'accounts/register.html')


def login(request):
    if request.method == 'POST':
        #login user
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid username and password')
            return redirect('login')     
    else:
        return render(request,'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'You are now logged out')
        return redirect('index')

def dashboard(request):
    user_contracts=Contract.objects.order_by('-contract_date').filter(user_id=request.user.id)
    context={
        'contracts':user_contracts,
    }
    return render(request,'accounts/dashboard.html',context)



