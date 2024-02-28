# user_auth/views.py
from django.contrib.auth.decorators import login_required 
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse
# Create your views here.
@login_required
def index(request):
    """
    View function for rendering the index page.

    Requires the user to be logged in.

    Args:
        request: The HTTP request object.

    Returns:
        Rendered HTML template for the index page.
    """
<<<<<<< HEAD
=======

>>>>>>> 0159f9ebaaecdbde88f816b4c817922f12295997
    return render(request, "user_auth/index.html")


def about(request):
    """
    View function for rendering the about page.

    Args:
        request: The HTTP request object.

    Returns:
        Rendered HTML template for the about page.
    """
    return render(request, "user_auth/about.html")


def contact(request):
    """
    View function for rendering the contact page.

    Args:
        request: The HTTP request object.

    Returns:
        Rendered HTML template for the contact page.
    """
    return render(request, "user_auth/contact.html")


def register_user(request):
    """
    View function for user registration.

    If the request method is POST, processes the registration form.
    If the form is valid, registers the user and logs them in.
    Redirects to the login page upon successful registration.

    Args:
        request: The HTTP request object.

    Returns:
        Rendered HTML template for the registration page.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_auth:login')
    else:
        form = UserCreationForm()
    return render(request, 'user_auth/register.html', {'form': form})



def logout_user(request):
    """
    View function for user logout.

    Logs out the currently authenticated user.

    Args:
        request: The HTTP request object.

    Returns:
        Redirects to the login page.
    """
    logout(request)
    return redirect('user_auth:login')

# user_auth/views.py
def login_user(request):
    """
    View function for user login.

    If the request method is POST, processes the login form.
    If the form is valid, logs the user in and redirects to the index page.

    Args:
        request: The HTTP request object.

    Returns:
        Rendered HTML template for the login page.
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Redirect to the polls app or any other desired URL
            return redirect('user_auth:index')  # Assuming 'polls:index' is the URL name for the polls index view
    else:
        form = AuthenticationForm()
    return render(request, 'user_auth/login.html', {'form': form})


# Create your views here.
