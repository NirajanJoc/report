
import user_account
from django.shortcuts import render, reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseRedirect

# Create your views here.

def signin_view(request):
    form=AuthenticationForm(request.POST or None)
    if request.POST:
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            return HttpResponseRedirect(reverse('calculator:dashboard_login'))
    context={'form':form}
    return render(request, 'login.html', context)

def signup_view(request):
    return render(request, 'register.html')