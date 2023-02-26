from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request, 'survey_server/index.html')

def customer(request):
    return render(request, 'survey_server/customer.html')
def manager(request):
    return render(request, 'survey_server/manager.html')
def profile(request):
    return render(request, 'survey_server/profile.html')


# Create your views here.
