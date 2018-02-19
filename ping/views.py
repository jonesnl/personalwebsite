from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from django.template import loader
from django.urls import reverse

from .models import Ping

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

@login_required(login_url='/ping/accounts/login')
def test_view(request):
    if request.method == 'GET':
        template = loader.get_template('ping/index.html')
        return HttpResponse(template.render(request=request))
    elif request.method == 'POST':
        ping_obj = get_object_or_404(Ping, user=request.user)
        ping_obj.pinging = True
        ping_obj.save()
        return HttpResponseRedirect(reverse('ping'))
