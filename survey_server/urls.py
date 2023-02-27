from django.urls import path
from survey_server import views

app_name = 'survey_server'

urlpatterns = [
path('', views.index, name='index'),
path('customer/', views.customer, name='customer'),
path('manager/', views.manager, name='manager'),
path('profile/', views.profile, name='profile'),
path('question1/', views.question1, name='question1'),
path('question2/', views.question2, name='question2'),
path('question3/', views.question3, name='question3'),
path('question4/', views.question4, name='question4'),
path('question5/', views.question5, name='question5'),
path('question6/', views.question6, name='question6'),
path('login/', views.login, name='login'),
path('register/', views.register, name='register'),
]