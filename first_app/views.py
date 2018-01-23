from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'first_app\index.html')

def asset(request):
    return render(request,'first_app\asset.html')

def transaction(request):
    return render(request,'first_app\transaction.html')

def trade(request):
    return render(request,'first_app\trade.html')
