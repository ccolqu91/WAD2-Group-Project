import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wad2_group_project.settings")

import django
django.setup()

from survey_server.models import User, Customer, Manager, Restaurant, Survey, Voucher

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

survery_data = [
    {
      "max_score": 20
    },
    {
      "max_score": 10
    },
]

voucher_data = [
    {
      "vocher_code": "1234",
      "value": "100",
      "issue_date": datetime.datetime.now(),
      "is_valid": True,
    },
    {
      "vocher_code": "1235",
      "value": "1000",
      "issue_date": datetime.datetime.now(),
      "is_valid": False,
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
    customer_instance.user = user_instances[0]
    customer_instance.save()

    print("Populating Manager \n")
    manager_instance = Manager(**manager_data)
    manager_instance.user = user_instances[0]
    manager_instance.save()

    print("Populating Restaurant data \n")
    restaurant_instances = []
    for data in restaurant_data:
        restaurant = Restaurant(**data)
        restaurant.manager = user_instances[1]
        restaurant_instances.append(restaurant)
    Restaurant.objects.bulk_create(restaurant_instances)

    print("Populating Survey data \n")
    survey_instances = []
    for data in survery_data:
        survey = Survey(**data)
        survey.customer = user_instances[0]
        survey.restaurant = restaurant_instances[0]
        survey_instances.append(survey)
    Survey.objects.bulk_create(survey_instances)

    print("Populating Voucher data \n")
    voucher_instances = []
    for i, data in enumerate(voucher_data):
        voucher = Voucher(**data)
        voucher.survey = survey_instances[i]
        voucher.customer = customer_instance
        voucher.restaurant = restaurant_instances[0]
        voucher_instances.append(voucher)
    Voucher.objects.bulk_create(voucher_instances)

    print("Done")


if __name__ == "__main__":
    populate()
