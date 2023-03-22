import json
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.http import JsonResponse
from survey_server.models import Survey
from survey_server.forms import *
from .decorators import *
from .score import *
from .voucher import *
import datetime
from .menu import *
from dateutil.relativedelta import relativedelta
from django.db.models import Avg
from django.db.models import Count



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




@manager_required
def manager(request):
    has_restaurant = Restaurant.objects.filter(manager=request.user).exists()
    print(has_restaurant)
    context = {'has_restaurant':has_restaurant}
    if has_restaurant:
        my_restaurant=Restaurant.objects.get(manager=request.user)
        context['has_restaurant']=has_restaurant
        context['restaurant']=my_restaurant.__dict__
        has_surveys=Survey.objects.filter(restaurant=my_restaurant).exists()
        if has_surveys:
            avg_scores = Survey.objects.filter(restaurant=my_restaurant).aggregate(
                                                avg_food_quality_score=Avg('food_quality_score'),
                                                avg_customer_service_score=Avg('customer_service_score'),
                                                avg_hygiene_score=Avg('hygiene_score'),
                                                avg_value_for_money_score=Avg('value_for_money_score'),
                                                avg_menu_variety_score=Avg('menu_variety_score'),
            )
            print(avg_scores)
            if avg_scores != None:
                context['avg_scores']= avg_scores

                starter_data_exists = Survey.objects.filter(restaurant=my_restaurant).exclude(starter_order=0).exists()
                if starter_data_exists:         
                    most_frequent_starter = Survey.objects.filter(restaurant=my_restaurant).annotate(
                        count=Count('starter_order')
                    ).order_by('-count').first().starter_order
                    top_starter = MenuItem.objects.get(id = most_frequent_starter).name
                    context['top_starter'] = top_starter

                main_data_exists = Survey.objects.filter(restaurant=my_restaurant).exclude(main_order=0).exists()
                if main_data_exists:       
                    most_frequent_main = Survey.objects.filter(restaurant=my_restaurant).annotate(
                        count=Count('main_order')
                    ).order_by('-count').first().main_order
                    top_main = MenuItem.objects.get(id = most_frequent_main).name
                    context['top_main'] = top_main
          
                dessert_data_exists = Survey.objects.filter(restaurant=my_restaurant).exclude(dessert_order=0).exists()
                if dessert_data_exists:     
                    most_frequent_dessert = Survey.objects.filter(restaurant=my_restaurant).annotate(
                        count=Count('dessert_order')
                    ).order_by('-count').first().dessert_order
                    top_dessert = MenuItem.objects.get(id = most_frequent_dessert).name
                    context['top_dessert'] = top_dessert

                drink_data_exists = Survey.objects.filter(restaurant=my_restaurant).exclude(drink_order=0).exists()
                if drink_data_exists:     
                    most_frequent_drink = Survey.objects.filter(restaurant=my_restaurant).annotate(
                        count=Count('drink_order')
                    ).order_by('-count').first().drink_order
                    top_drink = MenuItem.objects.get(id = most_frequent_drink).name
                    context['top_drink'] = top_drink

                context['starter_data_exists'] = starter_data_exists
                context['main_data_exists'] = main_data_exists
                context['dessert_data_exists'] = dessert_data_exists
                context['drink_data_exists'] = drink_data_exists

        context['has_surveys'] = has_surveys
        print("context:" +str(context))
    return render(request, 'survey_server/manager.html', context)

@login_required
def profile(request):
    context={}
    if request.user.user_type == 1: # customer
        customer = Customer.objects.get(user=request.user)
        profile_instance = Customer.objects.get(user=request.user).__dict__
        form = CustomerProfileForm(initial=profile_instance)
        if request.method == "POST":
            form = CustomerProfileForm(request.POST, request.FILES)
            if form.is_valid():
                new_info = form.save(commit = False)
                customer.user = request.user
                customer.bio = new_info.bio
                customer.profile_picture = new_info.profile_picture
                customer.save()
    elif request.user.user_type == 2: # manager
        has_restaurant = Restaurant.objects.filter(manager=request.user).exists()
        if has_restaurant:
            restaurant = Restaurant.objects.get(manager=request.user)
            context['has_restaurant']=has_restaurant
            context['restaurant']=restaurant.__dict__
        manager = Manager.objects.get(user=request.user)
        profile_instance = Manager.objects.get(user=request.user).__dict__
        form = ManagerProfileForm(initial=profile_instance)
        if request.method == "POST":
            form = ManagerProfileForm(request.POST, request.FILES)
            form.user = request.user
            if form.is_valid():
                new_info = form.save(commit = False)
                manager.user = request.user
                manager.bio = new_info.bio
                manager.profile_picture = new_info.profile_picture
                manager.save()
    context['form']= form
    return render(request, 'survey_server/profile.html',context)

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

    context= {'form': form, 'restaurant': restaurant.name, 'page_id' : page_id,'restaurant_slug' : restaurant_slug, 'about' : restaurant.about}
    return render(request, 'survey_server/survey.html', context=context)

@customer_required
def survey_success(request, restaurant_slug, survey_id):
    current_survey = Survey.objects.get(id=survey_id)
    scores_list = CalculateScore(current_survey)
    
    if not current_survey.voucher_code:
        voucher_code=get_voucher()
    else:
        voucher_code=current_survey.voucher_code

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
            return redirect(reverse('survey_server:manager'))
    else:
        form = AddRestaurant()

    return render(request, 'survey_server/add_restaurant.html',{'form':form})

@manager_required
def edit_restaurant(request):
    editing=True
    restaurant = Restaurant.objects.get(manager=request.user)
    restaurant_instance = Restaurant.objects.get(manager=request.user).__dict__
    form = EditRestaurant(initial=restaurant_instance)
    if request.method == "POST":
        form = EditRestaurant(request.POST, request.FILES)
        form['voucher_value'].initial = restaurant.voucher_value
        form.manager = request.user
        if form.is_valid():
            new_info = form.save(commit = False)
            restaurant.manager = request.user
            restaurant.name = new_info.name
            restaurant.about = new_info.about
            restaurant.logo = new_info.logo
            restaurant.menu = new_info.menu
            restaurant.voucher_value = new_info.voucher_value
            restaurant.slug = slugify(restaurant.name)
            restaurant.save()
            return redirect(reverse("survey_server:profile"))

    return render(request, 'survey_server/add_restaurant.html',{'form': form,'editing':editing})

@customer_required
def customer(request):
    surveys = Survey.objects.filter(customer=request.user)
    
    """ check if any voucher is older than 3 months
    if yes, make it invalid """
    today = datetime.date.today()
    if Survey.objects.filter(customer=request.user).exists():
        for survey in surveys:
            #print(survey.voucher_issue_date)
            if survey.voucher_issue_date != None and survey.voucher_issue_date + relativedelta(months=3) < today:
                survey.voucher_is_valid = False
                survey.save()
    profile= Customer.objects.get(user=request.user)
    vouchers = []
    for survey in surveys:
        if survey.voucher_code and survey.voucher_is_valid:
            voucher_dict = {
                'Voucher': survey.voucher_code,
                'Restaurant': survey.restaurant.name,
                'value' : survey.voucher_value,
                # 'expiry' : survey.voucher_issue_date + relativedelta(months=3)
            }
            vouchers.append(voucher_dict)
    return render(request, 'survey_server/customer.html', {'vouchers': vouchers,
                                                            'profile': profile})


