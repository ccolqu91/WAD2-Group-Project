from django.urls import path
from survey_server import views

app_name = 'survey_server'

urlpatterns = [
path('', views.index, name='index'),
path('/customer', views.customer, name='customer'),
path('/manager', views.manager, name='manager'),
path('/profile', views.profile, name='profile'),
path('/question1', views.question1, name='question1'),
]