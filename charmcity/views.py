from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
import json








def index(request):
    return render(request , 'index.html')

def signup(request):
    users = User.objects.all()
    a = ' '.join(i.username for i in users)
    all_users = a.split()
    json_data = json.dumps(all_users)
    return render(request, 'signup.html', {'users': json_data})