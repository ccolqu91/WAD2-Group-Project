from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Customer(models.Model):
    # id = models.IntegerField(primary_key=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_picture = models.ImageField(default = 0)
    bio = models.TextField(default=0)
    def __str__(self):
        return self.user.userName


class Manager(models.Model):
    # id = models.IntegerField(primary_key=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_picture = models.ImageField(default = 0)
    bio = models.TextField(default=0)
    def __str__(self):
        return self.user.userName
    

class User(models.Model):
    # id = models.IntegerField(primary_key=True)
    userName = models.CharField(max_length=128,unique = True)
    email = models.EmailField(max_length=128,unique = True)
    password = models.CharField(max_length=128,unique = True)
    user_type = models.PositiveSmallIntegerField(default = 0)
    def __str__(self):
        return self.userName
    

class Restaurant(models.Model):
    # id = models.IntegerField(primary_key=True)
    manager = models.ForeignKey(Manager,on_delete=models.CASCADE)
    logo = models.ImageField(default = 0)
    cuisine = models.CharField(max_length=128)
    about = models.TextField(null =0,blank = True)
    def __str__(self):
        return str(self.manager) + "'s Restaurant"


class Survey(models.Model):
    # id =  models.IntegerField(primary_key=True)
    customer =  models.ForeignKey(Customer, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant,on_delete = models.CASCADE)
    voucher = models.OneToOneField('Voucher', on_delete=models.CASCADE,null = True,blank =True,related_name='surveys')
    max_score = models.IntegerField(default  = 0)
    final_score = models.IntegerField(default = 0)

    ordered_starter = models.CharField(max_length=128,default = 0)
    starter_time = models.CharField(max_length=128,default = 0 )
    size_starter = models.CharField(max_length=128, default = 0)
    presentation_starter = models.CharField(max_length=128,default = 0)
    variety_starter = models.CharField(max_length=128,default = 0 )


    def __str__(self):
        return str(self.customer) + "'s Survey for " + str(self.restaurant)



class Voucher(models.Model):
    # id = models.IntegerField(primary_key=True)
    survey = models.OneToOneField('Survey',on_delete=models.CASCADE,related_name='vouchers')
    customer =  models.ForeignKey(Customer, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant,on_delete = models.CASCADE)
    vocher_code= models.CharField(max_length=128, null=True, blank=True)
    value = models.IntegerField(default = 0)
    issue_date = models.DateField(null=True, blank=True)
    is_valid = models.BooleanField(default=True)
    def __str__(self):
        return "Voucher for " + str(self.customer) + " at " + str(self.restaurant)


"""
I don't think we need this model since we have the Customer and Manager models which serve as profiles
"""
# class UserProfile(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     website = models.URLField(blank=True)
#     picture = models.ImageField(upload_to='profile_images',blank=True)

#     def __str__(self):
#         return self.user.userName + "'s Profile"


