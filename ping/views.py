from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from django.template import loader
from django.urls import reverse

from .models import Ping

@login_required(login_url='/ping/accounts/login')
def test_view(request):
    if request.method == 'GET':
        template = loader.get_template('ping/index.html')
        pinging_list = (Ping.objects
                            .filter(pinging=True)
                            .exclude(user=request.user))
        context = {
            'pinging_list': pinging_list,
        }
        return HttpResponse(template.render(request=request, context=context))
    elif request.method == 'POST':
        ping_obj = get_object_or_404(Ping, user=request.user)
        ping_obj.pinging = True
        ping_obj.save()
        return HttpResponseRedirect(reverse('ping'))
