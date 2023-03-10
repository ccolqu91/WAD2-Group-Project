from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify


class User(AbstractUser):
    USER_TYPE_CHOICES = (
		(1, 'customer'),
		(2, 'manager'),
	)

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, blank=True, default = 1)
    def __str__(self):
        return self.username

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True, related_name = 'customer')
    profile_picture = models.ImageField(default = 0)
    bio = models.TextField(default=0)
    def __str__(self):
        return self.user.username


class Manager(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True, related_name ='manager')
    profile_picture = models.ImageField(default = 0)
    bio = models.TextField(default=0)
    def __str__(self):
        return self.user.username
    


class Restaurant(models.Model):
    manager = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    logo = models.ImageField(default = 0)
    cuisine = models.CharField(max_length=128)
    about = models.TextField(null =0,blank = True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        self.slug = slugify(self.name)
        return str(self.manager) + "'s Restaurant " + str(self.name)


    
class Survey(models.Model):
    customer =  models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant,on_delete = models.CASCADE)
    voucher_code= models.CharField(max_length=128, null=True, blank=True)
    voucher_value = models.IntegerField(default = 0)
    voucher_issue_date = models.DateField(null=True, blank=True)
    voucher_is_valid = models.BooleanField(default=True)
    max_score = models.IntegerField(default  = 0)
    final_score = models.IntegerField(default = 0)

    # Starter Variables
    ordered_starter = models.CharField(max_length=128,default = 0)
    time_starter = models.CharField(max_length=128,default = 0 )
    size_starter = models.CharField(max_length=128, default = 0)
    presentation_starter = models.CharField(max_length=128,default = 0)
    variety_starter = models.CharField(max_length=128,default = 0 )

    # MainCourse Variables
    ordered_maincourse = models.CharField(max_length=128,default = 0)
    time_maincourse = models.CharField(max_length=128,default = 0 )
    size_maincourse = models.CharField(max_length=128, default = 0)
    presentation_maincourse = models.CharField(max_length=128,default = 0)
    variety_maincourse = models.CharField(max_length=128,default = 0 )

    # Dessert Variables
    ordered_dessert = models.CharField(max_length=128,default = 0)
    time_dessert = models.CharField(max_length=128,default = 0 )
    size_dessert = models.CharField(max_length=128, default = 0)
    presentation_dessert = models.CharField(max_length=128,default = 0)
    variety_dessert = models.CharField(max_length=128,default = 0 )

    # Drinks Variables
    ordered_drink = models.CharField(max_length=128,default = 0)
    time_drink = models.CharField(max_length=128,default = 0 )
    size_drink = models.CharField(max_length=128, default = 0)
    presentation_drink = models.CharField(max_length=128,default = 0)
    variety_drink = models.CharField(max_length=128,default = 0 )

    # Greeting Variables
    greeting_entry = models.CharField(max_length=128,default = 0 )
    greeting_waiting = models.CharField(max_length=128,default = 0 )
    greeting_clean = models.CharField(max_length=128,default = 0 )
    greeting_order = models.CharField(max_length=128,default = 0 )

    # Restroom Variables
    use_restroom = models.CharField(max_length=128,default = 0 )
    restroom_clean = models.CharField(max_length=128,default = 0 )
    missing_restroom = models.CharField(max_length=128,default = 0 )

    # Other Variables
    clean_restaurant = models.CharField(max_length=128,default = 0 )
    pay_bill_restaurant = models.CharField(max_length=128,default = 0 )
    service_staff = models.CharField(max_length=128,default = 0 )

    # Scoring Variables - actual scores for this survey
    food_quality_score = models.IntegerField(default = 0)
    customer_service_score = models.IntegerField(default = 0)
    hygiene_score  = models.IntegerField(default = 0)
    value_for_money_score = models.IntegerField(default = 0)
    menu_variety_score = models.IntegerField(default = 0)


    def __str__(self):
        return str(self.customer) + "'s Survey for " + str(self.restaurant)


