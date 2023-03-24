import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wad2_group_project.settings")

import django
from django.conf import settings
django.setup()

from survey_server.models import User, Customer, Manager, Restaurant, Survey, MenuItem

import datetime

default_image_path = settings.MEDIA_ROOT

user_data = [
    {
        "first_name": "John",
        "last_name": "Cena",
        "username": "customer",
        "email": "customer@gmail.com",
        "user_type": 1,
        "password": "Weak.123",
    },
    {
        "first_name": "Peter",
        "last_name": "Jones",
        "username": "customer1",
        "email": "customer1@gmail.com",
        "user_type": 1,
        "password": "Weak.123",
    },
    {
        "first_name": "Jimmy",
        "last_name": "Neutron",
        "username": "manager1",
        "email": "manager@gmail.com",
        "user_type": 2,
        "password": "Weak.123",
    },
    {
        "first_name": "Bob",
        "last_name": "Builder",
        "username": "manager2",
        "email": "manager1@gmail.com",
        "user_type": 2,
        "password": "Weak.123",
    },
    {
        "first_name": "Tom",
        "last_name": "Jerry",
        "username": "manager3",
        "email": "manager2@gmail.com",
        "user_type": 2,
        "password": "Weak.123",
    },
    {
        "first_name": "Joe",
        "last_name": "Admin",
        "username": "admin",
        "email": "admin@gmail.com",
        "user_type": 2,
        "password": "Weak.123",
        "is_staff": True,
        "is_superuser": True,
    },
]

customer_data = {
    "bio": "This is demo customer bio",
    "profile_picture": os.path.join(default_image_path, "Restaurant-Customer-Loyalty.jpg").replace("\\","/")
}

manager_data = {
    "bio": "This is demo manager bio",
    "profile_picture": os.path.join(default_image_path, "restaurant-manager.jpg").replace("\\","/")
}

restaurant_data = [
    {
        "name": "Burger King",
        "logo": os.path.join(default_image_path, "logos", "burger-king.jpg").replace("\\","/"),
        "cuisine": "American",
        "about": "The most special burger and zingers of all time.",
        "slug": "burger-king",
    },
    {
        "name": "Crown Burger",
        "logo": os.path.join(default_image_path, "logos","crown-burger.jpg").replace("\\","/"),
        "cuisine": "Indian",
        "about": "We offer the biggest and the tastiest burger in the town.",
        "slug": "crown-burger",
    },
    {
        "name": "KFC",
        "logo": os.path.join(default_image_path, "logos", "kfc.png").replace("\\","/"),
        "cuisine": "American",
        "about": "We have a wide range of chicken fast foods available.",
        "slug": "kfc",
    },
]

menu_item_data = [
    {
        "name": "Small Fries",
        "type": "starters",
    },
    {
        "name": "Salad",
        "type": "starters",
    },
    {
        "name": "Cheese Dippers",
        "type": "starters",
    },
    {
        "name": "Chickenburger",
        "type": "mains",
    },
    {
        "name": "Double Cheeseburger",
        "type": "mains",
    },
    {
        "name": "Chicken Tenders",
        "type": "mains",
    },
    {
        "name": "Cake",
        "type": "desserts",
    },
    {
        "name": "Brownies",
        "type": "desserts",
    },
    {
        "name": "Muffins",
        "type": "desserts",
    },
    {
        "name": "Sprite",
        "type": "drinks",
    },
    {
        "name": "Cocacola",
        "type": "drinks",
    },
    {
        "name": "Pepsi",
        "type": "drinks",
    },
]

survey1_data = [
    {
        "voucher_code": "1234",
        "voucher_value": 15,
        "voucher_issue_date": datetime.datetime.now(),
        "voucher_is_valid": True,

        "ordered_starter": "yes",
        "time_starter": "normal",
        "size_starter": "Yes",
        "presentation_starter": "Great",
        "variety_starter": "",

        "greeting_entry": "Excellent",
        "greeting_waiting": "Great",
        "greeting_clean": "Great",
        "greeting_order": "yes",

        "use_restroom": "yes",
        "restroom_clean": "Somewhat",
        "missing_restroom": "no",

        "clean_restaurant": "great",
        "pay_bill_restaurant": "great",
        "service_staff": "poor",

        "food_quality_score": 10,
        "customer_service_score": 8,
        "hygiene_score": 9,
        "value_for_money_score": 10,
        "menu_variety_score": 10,
    },]

survey2_data = [
    {
        "voucher_code": "1235",
        "voucher_value": 20,
        "voucher_issue_date": datetime.datetime.now(),
        "voucher_is_valid": False,

        "ordered_maincourse": "Yes",
        "time_maincourse": "normal",
        "size_maincourse": "Yes",
        "presentation_maincourse": "Great",
        "variety_maincourse": "",

        "greeting_entry": "Excellent",
        "greeting_waiting": "Great",
        "greeting_clean": "Great",
        "greeting_order": "yes",

        "use_restroom": "yes",
        "restroom_clean": "Somewhat",
        "missing_restroom": "no",

        "clean_restaurant": "great",
        "pay_bill_restaurant": "great",
        "service_staff": "poor",

        "food_quality_score": 10,
        "customer_service_score": 8,
        "hygiene_score": 9,
        "value_for_money_score": 10,
        "menu_variety_score": 10,
    },
]


def populate():
    print("Populating User data \n")
    user_instances = []
    for data in user_data:
        user = User(**data)
        user.set_password(data["password"])
        user_instances.append(user)
    User.objects.bulk_create(user_instances)

    print("Populating Customers \n")
    customer_instance = Customer(**customer_data)
    customer_instance.user = User.objects.get(username='customer')
    customer_instance.save()

    customer_instance = Customer(**customer_data)
    customer_instance.user = User.objects.get(username='customer1')
    customer_instance.save()

    print("Populating Managers \n")
    manager_instance = Manager(**manager_data)
    manager_instance.user = User.objects.get(username='manager1')
    manager_instance.save()

    manager_instance = Manager(**manager_data)
    manager_instance.user = User.objects.get(username='manager2')
    manager_instance.save()

    manager_instance = Manager(**manager_data)
    manager_instance.user = User.objects.get(username='manager3')
    manager_instance.save()

    print("Populating Restaurant data \n")
    restaurant_instances = []
    for i, data in enumerate(restaurant_data):
        restaurant = Restaurant(**data)
        restaurant.manager = User.objects.get(username=f'manager{i+1}')
        restaurant_instances.append(restaurant)
    Restaurant.objects.bulk_create(restaurant_instances)

    print("Populating Menu Items data \n")
    menu_item_instances = []
    for restaurant in Restaurant.objects.all():
        for data in menu_item_data:
            item = MenuItem(**data)
            item.restaurant = restaurant
            menu_item_instances.append(item)
    MenuItem.objects.bulk_create(menu_item_instances)

    print("Populating Survey data \n")
    survey_instances = []
    for data in survey1_data:
        survey = Survey(**data)
        survey.customer = User.objects.get(username='customer')
        survey.restaurant = Restaurant.objects.get(slug="burger-king")
        survey.starter_order = MenuItem.objects.filter(name = menu_item_instances[0].name).latest('id').id
        survey.main_order = MenuItem.objects.filter(name = menu_item_instances[5].name).latest('id').id
        survey.dessert_order = MenuItem.objects.filter(name = menu_item_instances[7].name).latest('id').id
        survey.drink_order = MenuItem.objects.filter(name = menu_item_instances[-1].name).latest('id').id
        survey_instances.append(survey)

    for data in survey2_data:
        survey = Survey(**data)
        survey.customer = User.objects.get(username='customer1')
        survey.restaurant = Restaurant.objects.get(slug="burger-king")
        survey.starter_order = MenuItem.objects.filter(name = menu_item_instances[0].name).latest('id').id
        survey.main_order = MenuItem.objects.filter(name = menu_item_instances[5].name).latest('id').id
        survey.dessert_order = MenuItem.objects.filter(name = menu_item_instances[7].name).latest('id').id
        survey.drink_order = MenuItem.objects.filter(name = menu_item_instances[-1].name).latest('id').id
        survey_instances.append(survey)
    Survey.objects.bulk_create(survey_instances)

    print("Done")

if __name__ == "__main__":
    populate()
