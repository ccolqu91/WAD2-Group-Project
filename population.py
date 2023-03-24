import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wad2_group_project.settings")

import django
django.setup()

from survey_server.models import User, Customer, Manager, Restaurant, Survey, MenuItem

import datetime

default_image_path = "default.png"

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
    "bio": "This is demo bio",
    "profile_picture": default_image_path,
}

manager_data = {
    "bio": "This is demo bio",
    "profile_picture": default_image_path,
}

restaurant_data = [
    {
        "name": "Burger King",
        "logo": default_image_path,
        "cuisine": "Korean",
        "about": "The most special burger and zingers of all time.",
        "slug": "burger-king",
    },
    {
        "name": "Crown Burger",
        "logo": default_image_path,
        "cuisine": "Indian",
        "about": "We offer the biggest and the tastiest burger in the town.",
        "slug": "crown-burger",
    },
    {
        "name": "KFC",
        "logo": default_image_path,
        "cuisine": "German",
        "about": "We have a wide range of chicken fast foods available.",
        "slug": "kfc",
    },
]

menu_item_data = [
    {
        "name": "Burger",
        "type": "starters",
    },
    {
        "name": "Zinger",
        "type": "starters",
    },
    {
        "name": "Broast",
        "type": "starters",
    },
    {
        "name": "Briyani",
        "type": "mains",
    },
    {
        "name": "Palao",
        "type": "mains",
    },
    {
        "name": "Chinese Rice",
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
        "name": "Spirit",
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

survery_data = [
    {
        "voucher_code": "1234",
        "voucher_value": 100,
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
    },
    {
        "voucher_code": "1235",
        "voucher_value": 100,
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

    print("Populating Customer \n")
    customer_instance = Customer(**customer_data)
    customer_instance.user = User.objects.get(username='customer')
    customer_instance.save()

    print("Populating Manager \n")
    manager_instance = Manager(**manager_data)
    manager_instance.user = User.objects.get(username='manager1')
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
        print(restaurant)
        print(Restaurant.objects.all())
        for data in menu_item_data:
            item = MenuItem(**data)
            item.restaurant = restaurant
            menu_item_instances.append(item)
    MenuItem.objects.bulk_create(menu_item_instances)

    print("Populating Survey data \n")
    survey_instances = []
    for data in survery_data:
        survey = Survey(**data)
        survey.customer = User.objects.get(username='customer')
        survey.restaurant = restaurant_instances[0]
        survey.starter_order = menu_item_instances[0].id
        survey.main_order = menu_item_instances[5].id
        survey.dessert_order = menu_item_instances[7].id
        survey.drink_order = menu_item_instances[-1].id
        survey_instances.append(survey)
    Survey.objects.bulk_create(survey_instances)

    print("Done")

if __name__ == "__main__":
    populate()
