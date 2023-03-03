from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from survey_server.forms import *
from survey_server.models import *


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

def select_restaurant(request):
    if request.POST:
        form = SelectRestaurant(request.POST)
    else:
        form = SelectRestaurant()

    return render(request, 'survey_server/select_restaurant.html',{'form':form})

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
    

def survey(request, restaurant_slug, page_id):
    try:
        restaurant = Restaurant.objects.get(slug=restaurant_slug)

    except Restaurant.DoesNotExist:
        restaurant = None
    
    if restaurant is None:
        return redirect('home')
    
    elif page_id < 22:
        form = form_dict[page_id]()
        if request.method == 'POST':
            form = form_dict[page_id](request.POST)

            if form.is_valid():
                if restaurant:
                    form.instance.restaurant = restaurant
                    form.instance.customer = User.objects.get(id=request.user.id)
                    form.instance.customer_id = request.user.id
                    answer_dict = form.cleaned_data
                    created = Survey.objects.update_or_create(customer=request.user, restaurant= restaurant, defaults=answer_dict)[1]
                    print(created)
                    if page_id < 22:
                        return redirect(reverse('survey_server:survey',
                                            kwargs={'restaurant_slug':
                                                restaurant_slug, 'page_id' : page_id + 1}))

            else:
                print(form.errors)

    else:
        return HttpResponse("Survey complete!")

    context_dict = {'form': form, 'restaurant': restaurant.name, 'page_id' : page_id}
    return render(request, 'survey_server/question1.html', context=context_dict)


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('survey_server:index'))