from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages





# Create your views here.
def signup(request):
    user = None
    error_message = None 
    if request.method == 'POST':
        user_name = request.POST['username']
        user_password = request.POST['password1']
        try:
            user = User.objects.create_user(
            username=user_name,
            password=user_password

        )
        except Exception as e:
            error_message = str(e)

    return render(request, 'user_signup.html',{'user':user,'error_message':error_message})



def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {username} 👋")
            return redirect('index')
        else:
            messages.error(request, "Invalid username or password. Please try again.")
            return redirect('signin')  # refresh the same page with error
    return render(request, 'user_signin.html')

def signout(request):
    logout(request)
    return redirect('index')   
