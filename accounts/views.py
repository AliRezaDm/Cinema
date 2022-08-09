from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            # login was a success
            login(request, user)
            return HttpResponseRedirect(reverse('ticketing:movie_list'))
        else:
            # in case of undifined user or wrong pass word
            context = {
                'username' : username,
                'error' : 'User was not FOUND!!'
            }
            
    else:
        context = {}
    return render(request, 'accounts/login_view.html', context)

def logout_view(request):
    logout (request)
    return HttpResponseRedirect(reverse('accounts:login'))
    

@login_required
def profile_details(request):
    profile = request.user.profile
    context = {
        'profile' : profile
    }
    return render(request, 'profile_view.html', context)


