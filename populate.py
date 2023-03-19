import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wad2_group_project.settings')

import django
django.setup()

from survey_server.models import User, Customer, Manager, Restaurant

user_data = [
  {
    "first_name": "John",
    "last_name": "Cena",
    "username": "customer",
    "email": "customer@gmail.com",
    "user_type": 1,
    "password": "Weak.123"
  },
  {
    "first_name": "Jimmy",
    "last_name": "Neutron",
    "username": "manager",
    "email": "manager@gmail.com",
    "user_type": 2,
    "password": "Weak.123"
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
}

manager_data = {
  "bio": "This is demo bio",
}

restaurant_data = [
  {
    "name": "Restaurant X",
    "cuisine": "This is cuisine",
    "about": "This is about",
    "slug": "restaurant-x",
  },
  {
    "name": "Restaurant Y",
    "cuisine": "This is cuisine",
    "about": "This is about",
    "slug": "restaurant-y",
  },
  {
    "name": "Restaurant Z",
    "cuisine": "This is cuisine",
    "about": "This is about",
    "slug": "restaurant-z",
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


    print("Done")

if __name__ == "__main__":
    populate()