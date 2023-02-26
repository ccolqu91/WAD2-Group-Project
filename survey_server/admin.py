from django.contrib import admin

from django.contrib import admin
from survey_server.models import Customer,Manager,Restaurant,User,Survey,Voucher,UserProfile


admin.site.register(Customer)
admin.site.register(Manager)
admin.site.register(Restaurant)
admin.site.register(User)
admin.site.register(Survey)
admin.site.register(Voucher)
admin.site.register(UserProfile)


