from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect

# Create your views here.

def login_view(request):
    """Login user"""
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        print('SUCCESS you logged in!')
        # redirect to success page...
        return redirect('test_view')
    else:
        # return invalid login msg
        return HttpResponse('FAILED to login bro')

def logout_view(requst):
    """Logout user"""
    logout(request)
    print('successful logout')
    # redirect to success page

@login_required
def test_view(request):
    return HttpResponse('hello world!')
