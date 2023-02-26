from django.shortcuts import render
from django.http import HttpResponse
from survey_server.forms import Question1Form

def index(request):
    return render(request, 'survey_server/index.html')

def customer(request):
    return render(request, 'survey_server/customer.html')
def manager(request):
    return render(request, 'survey_server/manager.html')
def profile(request):
    return render(request, 'survey_server/profile.html')

def question1(request):
    form = Question1Form()
    return render(request, 'survey_server/question1.html', {'form': form})

# Create your views here.
