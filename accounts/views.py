from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .forms import LoginForm,UserRegistrationForm
from .models import Profile
def sign_in(request):
    if request.method == 'POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username, password=password)
            
            if user is not None and user.is_active:
                login(request, user)
                messages.info(request,'Log in request was successfully received')
                return redirect('shop:list')
 
        messages.error(request,'Invalid Username or Password')
    form=LoginForm()
    return render(request,'accounts/login.html',{'form':form})



def sign_up(request):
    if request.method == 'POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            Profile.objects.create(user=user)
            messages.info(request,'Your account was successfully created')
            return render(request,'accounts/register_done.html',{'user':user})
    else:
            # messages.error(request,'Please Correct the Following Error')
        form=UserRegistrationForm()
    return render(request,'accounts/register.html',{'form':form})

def sign_out(request):
    logout(request)
    messages.success(request,'Logout request was successful')
    return redirect('accounts:login')
