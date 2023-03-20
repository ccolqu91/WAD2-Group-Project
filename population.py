import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wad2_group_project.settings")

import django
django.setup()

from survey_server.models import User, Customer, Manager, Restaurant, Survey

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
        "username": "manager",
        "email": "manager@gmail.com",
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


def populate():
    print("Populating User data \n")
    user_instances = []
    for data in user_data:
        user = User(**data)
        user.set_password(data["password"])
        user_instances.append(user)
    User.objects.bulk_create(user_instances)

    # Get the customer user instance created above
    customer_user = User.objects.get(username='customer')

    print("Populating Customer \n")
    customer_instance = Customer(**customer_data)
    customer_instance.user = customer_user
    customer_instance.save()

    print("Populating Manager \n")
    manager_instance = Manager(**manager_data)
    manager_instance.user = User.objects.get(username='manager')
    manager_instance.save()

    print("Populating Restaurant data \n")
    restaurant_instances = []
    for i, data in enumerate(restaurant_data):
        restaurant = Restaurant(**data)
        restaurant.manager = User.objects.get(username='manager')
        restaurant.slug = f"{restaurant.slug}-{i+1}"
        restaurant_instances.append(restaurant)
    Restaurant.objects.bulk_create(restaurant_instances)

    # Get the restaurant instances created above
    burger_king = Restaurant.objects.get(slug='burger-king-1')
    crown_burger = Restaurant.objects.get(slug='crown-burger-2')
    kfc = Restaurant.objects.get(slug='kfc-3')

    print("Populating Survey data \n")
    # Create the survey instances with the customer user instance and the restaurant instances
    survey_instances = [
        Survey(
            customer=customer_user,
            restaurant=burger_king,
            food_quality_score=20,
            customer_service_score=20,
            hygiene_score=15,
            value_for_money_score=20,
            menu_variety_score=15,
            voucher_issue_date='2022-01-01' 
        ),
        Survey(
            customer=customer_user,
            restaurant=crown_burger,
            food_quality_score=10,
            customer_service_score=10,
            hygiene_score=5,
            value_for_money_score=10,
            menu_variety_score=5,
            voucher_issue_date='2022-01-01'
        ),
        Survey(
            customer=customer_user,
            restaurant=kfc,
            food_quality_score=15,
            customer_service_score=20,
            hygiene_score=10,
            value_for_money_score=15,
            menu_variety_score=10,
            voucher_issue_date='2022-01-01' 
        ),
    ]
    Survey.objects.bulk_create(survey_instances)

    print("Done")

if __name__ == "__main__":
    populate()
       
