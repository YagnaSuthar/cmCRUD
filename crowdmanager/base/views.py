from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def baseHome(request):
    return render(request,'base/base_home.html')

def loginPage(request):
    page = "login"
    if request.user.is_authenticated:
        return redirect('eventsHome')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username= username)
        except:
            # django flash messages
            messages.error(request,'User does not exits')

        user = authenticate(request,username=username,password= password)
        
        if user is not None:
            login(request,user)
            return redirect('eventsHome')
        else:
            messages.error(request,'Username or password does not exits')
    context ={'page':page}
    return render(request,'user_auth/login_register.html',context)


def logoutPage(request):
    logout(request)
    return redirect('baseHome')
    
def contact(request):
    return render(request,'base/contactus.html')

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower() 
            user.save()
            login(request,user)
            return redirect('eventsHome')
        else:
             messages.error(request,'There is error during registration')

    context ={
        'form':form,
    }
    return render(request,'user_auth/login_register.html',context)