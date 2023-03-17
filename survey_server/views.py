from collections import Counter
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.http import JsonResponse
from survey_server.models import Survey
from django.views.generic import View
from survey_server.forms import *
# from survey_server.models import *
from .decorators import *
from .score import *
from .voucher import *
import datetime
from .menu import *


form_dict = {1 : ChooseStarterForm,
             2 : StarterQuestionsForm,
             3 : VariertyStarterForm,
             4 : ChooseMainCourseForm,
             5 : MainCourseQuestionsForm, 
             6 : VariertyMainCourseForm, 
             7 : ChooseDessertForm,
             8 : DessertQuestionsForm,
             9 : VariertyDessertForm,
             10: ChooseDrinkForm, 
             11 : DrinkQuestionsForm,
             12 : VariertyDrinkForm,
             13 : GreetingEntryForm,
             14 : GreetingWaitingForm,
             15: GreetingCleanForm,
             16 : GreetingOrderForm,
             17 : UseRestroomForm,
             18: RestroomQuestionsForm,
             19 : RestaurantCleanForm,
             20 : RestaurantPayBillForm,
             21 : RestaurantServiceStaffForm}

def index(request):
    return render(request, 'survey_server/index.html')

def customer(request):
    return render(request, 'survey_server/customer.html')

def manager(request):
    return render(request, 'survey_server/manager.html')

def profile(request):
    return render(request, 'survey_server/profile.html')

def about(request):
    return render(request, 'survey_server/about.html')

@customer_required
def select_restaurant(request):
    if request.POST:
        form = SelectRestaurant(request.POST)
        restaurant = request.POST.get('restaurant')
    else:
        form = SelectRestaurant()
    restaurant = request.POST.get('restaurant')
    return render(request, 'survey_server/select_restaurant.html',{'form':form,'restaurant':restaurant})

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
    
@customer_required
def survey(request, restaurant_slug, page_id):
    try:
        restaurant = Restaurant.objects.get(slug=restaurant_slug)

    except Restaurant.DoesNotExist:
        restaurant = None
    
    if restaurant is None:
        return redirect('survey_server:index')
    
    elif page_id < 22:
        form = form_dict[page_id]()
        """ assigning choices that display on page """
        if page_id == 2: #starters form
            form.fields['starter_order'].choices = list(MenuItem.objects.filter(restaurant=restaurant,type='starters').values_list('id', 'name'))
        elif page_id == 5: #mains form
            form.fields['main_order'].choices = list(MenuItem.objects.filter(restaurant=restaurant,type='mains').values_list('id', 'name'))
        elif page_id == 8: #desserts form
            form.fields['dessert_order'].choices = list(MenuItem.objects.filter(restaurant=restaurant,type='desserts').values_list('id', 'name'))
        elif page_id == 11: #drinks form
            form.fields['drink_order'].choices = list(MenuItem.objects.filter(restaurant=restaurant,type='drinks').values_list('id', 'name'))
        if request.method == 'POST':
            form = form_dict[page_id](request.POST)
            """ assigning choices again when request.POST """
            if page_id == 2: #starters form
                form.fields['starter_order'].choices = list(MenuItem.objects.filter(restaurant=restaurant,type='starters').values_list('id', 'name'))
            elif page_id == 5: #mains form
                form.fields['main_order'].choices = list(MenuItem.objects.filter(restaurant=restaurant,type='mains').values_list('id', 'name'))
            elif page_id == 8: #desserts form
                form.fields['dessert_order'].choices = list(MenuItem.objects.filter(restaurant=restaurant,type='desserts').values_list('id', 'name'))
            elif page_id == 11: #drinks form
                form.fields['drink_order'].choices = list(MenuItem.objects.filter(restaurant=restaurant,type='drinks').values_list('id', 'name'))
            if form.is_valid():
                if restaurant:
                    form.instance.restaurant = restaurant
                    form.instance.customer = User.objects.get(id=request.user.id)
                    form.instance.customer_id = request.user.id
                    answer_dict = form.cleaned_data
                    Survey.objects.update_or_create(customer=request.user, restaurant= restaurant, defaults=answer_dict)
                    gatekeepers = ['ordered_starter', 'ordered_maincourse', 'ordered_dessert', 'ordered_drink', 'use_restroom']
                    if page_id in [1, 4, 7, 10, 17] and any(map(lambda param: param in request.POST and request.POST[param] == 'no', gatekeepers)):
                        return redirect(reverse('survey_server:survey',
                                            kwargs={'restaurant_slug':
                                                restaurant_slug, 'page_id' : page_id + 2}))
                    elif page_id < 22:
                        return redirect(reverse('survey_server:survey',
                                            kwargs={'restaurant_slug':
                                                restaurant_slug, 'page_id' : page_id + 1}))

            else:
                print(form.errors)

    else:
        survey_id = Survey.objects.filter(customer=request.user, restaurant=restaurant).latest('id').id
        return redirect(reverse('survey_server:survey_success',
                                            kwargs={'restaurant_slug':
                                                restaurant_slug, 'survey_id' : survey_id}))

    context= {'form': form, 'restaurant': restaurant.name, 'page_id' : page_id,'restaurant_slug' : restaurant_slug}
    return render(request, 'survey_server/survey.html', context=context)

@customer_required
def survey_success(request, restaurant_slug, survey_id):
    current_survey = Survey.objects.get(id=survey_id)
    scores_list = CalculateScore(current_survey)
    

    voucher_code=get_voucher()

    Survey.objects.update_or_create(id = survey_id, defaults = {'food_quality_score' : scores_list[0],
                                                                'customer_service_score'  : scores_list[1],
                                                                'hygiene_score' : scores_list[2],
                                                                'value_for_money_score' : scores_list[3],
                                                                'menu_variety_score' : scores_list[4],
                                                                'voucher_code' : voucher_code,
                                                                'voucher_is_valid' : True,
                                                                'voucher_issue_date' : datetime.date.today()})
    context = {'voucher_code': voucher_code}
    return render(request, 'survey_server/success.html', context)

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('survey_server:index'))

@manager_required
def add_restaurant(request):
    if request.POST:
        form = AddRestaurant(request.POST, request.FILES)
        if form.is_valid():
            restaurant = form.save(commit=False)
            restaurant.manager = request.user
            restaurant.slug = slugify(restaurant.name)
            restaurant.save()
            form.save_m2m()
            populate_menu_items(restaurant.slug)
            return redirect(reverse('manager'))
    else:
        form = AddRestaurant()

    return render(request, 'survey_server/add_restaurant.html',{'form':form})



# not sure if we need to add a new Score model in our models.py 
# because if we want let our chartjs chart change with the new data reecived 
# we need a view and a new model factor to link the data in database and chart we wanna show to our tutor

# def chart_data(request):
#     scores = Score.objects.all()
#     labels = [str(score.date) for score in scores]
#     values = [score.value for score in scores]
#     data = {
#         'labels': labels,
#         'values': values,
#     }
#     return JsonResponse(data)