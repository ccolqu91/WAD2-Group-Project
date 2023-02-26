from django.shortcuts import render
from django.shortcuts import redirect
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
    ordered_starter = None
    if request.method == 'POST':
        form = Question1Form(request.POST)
        if form.is_valid():
            ordered_starter = request.POST.get('ordered_starter')
            if ordered_starter == "yes":
                return redirect('survey_server:question2')
            else:
                return redirect('survey_server:question5')
    else:
        form = Question1Form()
    context = {'form': form, 'ordered_starter': ordered_starter}
    return render(request, 'survey_server/question1.html', context)



def question2(request):
    return render(request, 'survey_server/question2.html')


def question5(request):
    return render(request, 'survey_server/question5.html')

# Create your views here.
