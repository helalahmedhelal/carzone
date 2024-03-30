from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('home') 
        else:
             
            return redirect('login')
    else:  
        messages.error(request, 'Invalid login credentials')  
        return render(request,'account_pages/login.html')

def signup(request):
    if request.method == 'POST':
        
        
        firstname = request.POST['firstname']
        
        lastname = request.POST['lastname']
        
        username = request.POST['username']
        
        email = request.POST['email']
        
        password = request.POST['password']
        
        confirmpassword = request.POST['confirm_password']
        
        if password != confirmpassword:
           
            return render(request, 'account_pages/registration.html', {'error': 'Passwords do not match'})
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return render(request, 'account_pages/registration.html', {'error': 'Username already exists'})
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists!')
            return render(request, 'account_pages/registration.html', {'error': 'Email already exists'})
        
        try:
            user = User.objects.create_user(username=username, email=email, password=password, first_name=firstname, last_name=lastname)
            user.save()
            auth.login(request,user=user)
            # Optionally, log in the user here
            messages.success(request, 'You are registered successfully.')
            return redirect('home')  # Redirect to login page after successful registration
        except Exception as e:
            # Handle exceptions, e.g., database errors
            return render(request, 'account_pages/registration.html', {'error': 'An error occurred. Please try again.'})
        
    else:
        messages.error(request, 'Password do not match')
        return render(request, 'account_pages/registration.html')
    
    
def logout(request):
    if request.method=='POST':
       auth.logout(request)
       return redirect('home') 
    return redirect('home')    
    