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
        print("Trying login with:", username, password)

        user = authenticate(request, username=username, password=password)
        print("Authenticate returned:", user)

        if user is not None:
            login(request, user)
            print("✅ Login successful")
            return redirect('list')
        else:
            print("❌ Invalid login")
            messages.error(request, "Invalid username or password.")
            return render(request, 'user_signin.html')  # Show error on same page

    return render(request, 'user_signin.html')

def signout(request):
    logout(request)
    return redirect('index')   
