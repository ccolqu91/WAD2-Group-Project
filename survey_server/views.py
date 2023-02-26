from django.shortcuts import render, redirect
from survey_server.forms import Question1Form, Question2Form, Question3Form, Question4Form, Question5Form

def index(request):
    return render(request, 'survey_server/index.html')

def customer(request):
    return render(request, 'survey_server/customer.html')

def manager(request):
    return render(request, 'survey_server/manager.html')

def profile(request):
    return render(request, 'survey_server/profile.html')

def question1(request):
    if request.method == 'POST':
        form = Question1Form(request.POST)
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
            else:
                return redirect('survey_server:question5')
    else:
        form = Question1Form()

    context = {'form': form}

    return render(request, 'survey_server/question1.html', context)


def question2(request):
    if request.method == 'POST':
        form = Question2Form(request.POST)
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
        form = Question2Form()

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
        form = Question3Form(request.POST)
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
        form = Question3Form()

    context = {'form': form, 'food_quality_points': request.session.get('food_quality_points', 0),
               'customer_service_points': request.session.get('customer_service_points', 0),
               'hygiene_points': request.session.get('hygiene_points', 0),
               'value_for_money_points': request.session.get('value_for_money_points', 0),
               'menu_variety_points': request.session.get('menu_variety_points', 0)}
    return render(request, 'survey_server/question3.html', context)

def question4(request):
    if request.method == 'POST':
        form = Question4Form(request.POST)
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
        form = Question4Form()

    context = {'form': form, 'food_quality_points': request.session.get('food_quality_points', 0),
               'customer_service_points': request.session.get('customer_service_points', 0),
               'hygiene_points': request.session.get('hygiene_points', 0),
               'value_for_money_points': request.session.get('value_for_money_points', 0),
               'menu_variety_points': request.session.get('menu_variety_points', 0)}
    
    return render(request, 'survey_server/question4.html', context)

def question5(request):
    if request.method == 'POST':
        form = Question5Form(request.POST)
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
        form = Question5Form()

    context = {'form': form, 'food_quality_points': request.session.get('food_quality_points', 0),
               'customer_service_points': request.session.get('customer_service_points', 0),
               'hygiene_points': request.session.get('hygiene_points', 0),
               'value_for_money_points': request.session.get('value_for_money_points', 0),
               'menu_variety_points': request.session.get('menu_variety_points', 0)}
    
    return render(request, 'survey_server/question5.html',context)

def question6(request):

    return render(request, 'survey_server/question6.html')
