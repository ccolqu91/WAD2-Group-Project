from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from survey_server.forms import *

def index(request):
    return render(request, 'survey_server/index.html')

def customer(request):
    return render(request, 'survey_server/customer.html')

def manager(request):
    return render(request, 'survey_server/manager.html')

def profile(request):
    return render(request, 'survey_server/profile.html')

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            if user.user_type == 1:
                profile = Customer.objects.create(user=user)
            else:
                profile = Manager.objects.create(user=user)
            
            profile.save()
            login(request, user)
            registered = True
            messages.success(request, "Registration successful." )
            return redirect("index")

        else:
            print(user_form.errors)
    else:
        user_form = UserRegistrationForm()

    return render(request,
                'survey_server/register.html',
                context = {'form': user_form,
                        'registered': registered})


def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:

            if user.is_active:
                login(request, user)
                return redirect(reverse('survey_server:index'))
            else:
                return HttpResponse("Your Survey Server account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")

    

    else:
        return render(request, 'survey_server/login.html')

def question1(request):
    if request.method == 'POST':
        form = ChooseStarterForm(request.POST)
        if form.is_valid():
            ordered_starter = request.POST.get('ordered_starter')
            request.session['food_quality_points'] = 0
            request.session['customer_service_points'] = 0
            request.session['hygiene_points'] = 0
            request.session['value_for_money_points'] = 0
            request.session['menu_variety_points'] = 0

            if ordered_starter == "yes":
                request.session['customer_service_points'] = request.session.get('customer_service_points', 0) + 1
                return redirect('survey_server:question2')
            elif ordered_starter == "no":
                return redirect('survey_server:question5')
    else:
        form = ChooseStarterForm()

    context = {
    'form': form,
    'food_quality_points': request.session.get('food_quality_points', 0),
    'customer_service_points': request.session.get('customer_service_points', 0),
    'hygiene_points': request.session.get('hygiene_points', 0),
    'value_for_money_points': request.session.get('value_for_money_points', 0),
    'menu_variety_points': request.session.get('menu_variety_points', 0),
}

    return render(request, 'survey_server/question1.html', context)


def question2(request):
    if request.method == 'POST':
        form = StarterQuestionsForm(request.POST)
        if form.is_valid():
            starter_time = form.cleaned_data['starter_time']
            if starter_time == 'fast':
                request.session['customer_service_points'] = request.session.get('customer_service_points', 0) + 2
            elif starter_time == 'normal':
                request.session['customer_service_points'] = request.session.get('customer_service_points', 0) + 1
            elif starter_time == 'slow':
                request.session['customer_service_points'] = request.session.get('customer_service_points', 0) + 0
            return redirect('survey_server:question3')
    else:
        form = StarterQuestionsForm()

    context = {
    'form': form,
    'food_quality_points': request.session.get('food_quality_points', 0),
    'customer_service_points': request.session.get('customer_service_points', 0),
    'hygiene_points': request.session.get('hygiene_points', 0),
    'value_for_money_points': request.session.get('value_for_money_points', 0),
    'menu_variety_points': request.session.get('menu_variety_points', 0),
}


    return render(request, 'survey_server/question2.html', context)


def question3(request):
    if request.method == 'POST':
        form = StarterQuestionsForm(request.POST)
        if form.is_valid():
            size_starter = form.cleaned_data['size_starter']
            if size_starter == 'Great':
                request.session['value_for_money_points'] = request.session.get('value_for_money_points', 0) + 2
            elif size_starter == 'Somewhat':
                request.session['value_for_money_points'] = request.session.get('value_for_money_points', 0) + 1
            elif size_starter == 'NO':
                request.session['value_for_money_points'] = request.session.get('value_for_money_points', 0) + 0
            return redirect('survey_server:question4')
    else:
        form = StarterQuestionsForm()

    context = {'form': form, 'food_quality_points': request.session.get('food_quality_points', 0),
               'customer_service_points': request.session.get('customer_service_points', 0),
               'hygiene_points': request.session.get('hygiene_points', 0),
               'value_for_money_points': request.session.get('value_for_money_points', 0),
               'menu_variety_points': request.session.get('menu_variety_points', 0)}
    return render(request, 'survey_server/question3.html', context)

def question4(request):
    if request.method == 'POST':
        form = StarterQuestionsForm(request.POST)
        if form.is_valid():
            presentation_starter = form.cleaned_data['presentation_starter'] 
            if presentation_starter == 'Excellent':
                request.session['food_quality_points'] = request.session.get('food_quality_points', 0) + 4
            elif presentation_starter == 'Great':
                request.session['food_quality_points'] = request.session.get('food_quality_points', 0) + 2
            elif presentation_starter == 'Somewhat':
                request.session['food_quality_points'] = request.session.get('food_quality_points', 0) + 1
            elif presentation_starter == 'No':
                request.session['food_quality_points'] = request.session.get('food_quality_points', 0) + 0

            return redirect('survey_server:question5')
    else:
        form = StarterQuestionsForm()

    context = {'form': form, 'food_quality_points': request.session.get('food_quality_points', 0),
               'customer_service_points': request.session.get('customer_service_points', 0),
               'hygiene_points': request.session.get('hygiene_points', 0),
               'value_for_money_points': request.session.get('value_for_money_points', 0),
               'menu_variety_points': request.session.get('menu_variety_points', 0)}
    
    return render(request, 'survey_server/question4.html', context)

def question5(request):
    if request.method == 'POST':
        form = VariertyStarterForm(request.POST)
        if form.is_valid():
            variety_starter = form.cleaned_data['variety_starter']  
            if variety_starter == 'Excellent':
                request.session['menu_variety_points'] = request.session.get('menu_variety_points', 0) + 4
            elif variety_starter == 'Great':
                request.session['menu_variety_points'] = request.session.get('menu_variety_points', 0) + 2
            elif variety_starter == 'Somewhat':
                request.session['menu_variety_points'] = request.session.get('menu_variety_points', 0) + 1
            elif variety_starter == 'No':
                request.session['menu_variety_points'] = request.session.get('menu_variety_points', 0) + 0
            
            return redirect('survey_server:question6')
    else:
        form = VariertyStarterForm()

    context = {'form': form, 'food_quality_points': request.session.get('food_quality_points', 0),
               'customer_service_points': request.session.get('customer_service_points', 0),
               'hygiene_points': request.session.get('hygiene_points', 0),
               'value_for_money_points': request.session.get('value_for_money_points', 0),
               'menu_variety_points': request.session.get('menu_variety_points', 0)}
    
    return render(request, 'survey_server/question5.html',context)

def question6(request):

    return render(request, 'survey_server/question6.html')




@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('survey_server:index'))