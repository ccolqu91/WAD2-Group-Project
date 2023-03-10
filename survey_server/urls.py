from django.urls import path
from survey_server import views

app_name = 'survey_server'

urlpatterns = [
path('', views.index, name='index'),
path('customer/', views.customer, name='customer'),
path('manager/', views.manager, name='manager'),
path('profile/', views.profile, name='profile'),
path('survey/<slug:restaurant_slug>/<int:page_id>', views.survey, name='survey'),
path('survey_success/<slug:restaurant_slug>/<int:survey_id>', views.survey_success, name='survey_success'),
path('login/', views.user_login, name='login'),
path('register/', views.register, name='register'),
path('logout/', views.user_logout, name='logout'),
path('select/', views.select_restaurant, name='select')
]