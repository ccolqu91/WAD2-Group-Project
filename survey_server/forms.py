from django import forms
from .models import *


class UserRegistrationForm(forms.ModelForm):

    # This form asks if the user is registering as a customer or owner and asks for their details

    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(required=True)

    USER_REG_CHOICES = [
        (1,'customer'),
        (2,'manager'),
    ]
    user_type = forms.ChoiceField(
        label='Would you like to register as a customer or a restaurant manager?',
        choices=USER_REG_CHOICES,
        widget=forms.RadioSelect
    )

    class Meta:
        model = User
        fields = ('username', 'email','password','user_type',)
        help_texts = {
            'username': None,
			'email': None,
            'password': None,
        }

class SelectRestaurant(forms.Form):
    restaurant = forms.ChoiceField(choices=[(r.id, r.name) for r in Restaurant.objects.all()])

    class Meta:
        help_texts = {
            'restaurant': None,
        }

class ChooseStarterForm(forms.ModelForm):

    # This form is question one of the survey

    ORDERED_STARTER_CHOICES = [
        ('yes','yes'),
        ('no','no'),
    ]
    ordered_starter = forms.ChoiceField(
        label='Did you order a starter?',
        choices=ORDERED_STARTER_CHOICES,
        widget=forms.RadioSelect
    )

    class Meta:
        model = Survey
        fields = ('ordered_starter',)

class StarterQuestionsForm(forms.ModelForm):

    #This form is question 2 3 and 4 of the survey

    STARTER_TIME_CHOICES = [
        ('fast', '7-11 minutes or less'),
        ('normal', '11-16 minutes'),
        ('slow', '17 minutes or more'),
    ]
    time_starter = forms.ChoiceField(
        label='Roughly how long did it take for your starter to come once you had placed the order?',
        choices=STARTER_TIME_CHOICES,
        widget=forms.RadioSelect
    )
    SIZE_STARTER_CHOICES = [
        ('Yes', 'Yes'),
        ('Somewhat', 'Somewhat'),
        ('No', 'No'),
    ]
    size_starter = forms.ChoiceField(
        label='Would you agree your starter was a generous size?',
        choices=SIZE_STARTER_CHOICES,
        widget=forms.RadioSelect
    )
    PRESENTATION_STARTER_CHOICES = [
        ('Excellent','Excellent taste and presentation'),
        ('Great', 'Great taste and presentation'),
        ('Somewhat', 'Either the taste or the presentation let the meal down'),
        ('No', 'Both were poor'),
    ]
    presentation_starter = forms.ChoiceField(
        label='To what extent did you appreciate the presentation and taste of your starter?',
        choices=PRESENTATION_STARTER_CHOICES,
        widget=forms.RadioSelect
    )

    class Meta:
        model = Survey
        fields = ('time_starter','size_starter','presentation_starter',)


class VariertyStarterForm(forms.ModelForm):

    #This form is question 5 of the survey

    VARIETY_STARTER_CHOICES = [
        ('Excellent','Excellent variety'),
        ('Great', 'Great variety'),
        ('Somewhat', 'There was some variety'),
        ('No', 'I felt that there was no variety'),
    ]
    variety_starter = forms.ChoiceField(
        label='How did you find the variety of the starters menu?',
        choices=VARIETY_STARTER_CHOICES,
        widget=forms.RadioSelect
    )

    class Meta:
        model = Survey
        fields = ('variety_starter',)

class ChooseMainCourseForm(forms.ModelForm):

    # This form is question 6 of the survey

    ORDERED_MAINCOURSE_CHOICES = [
        ('yes','yes'),
        ('no','no'),
    ]
    ordered_maincourse = forms.ChoiceField(
        label='Did you order a Main Course?',
        choices=ORDERED_MAINCOURSE_CHOICES,
        widget=forms.RadioSelect
    )

    class Meta:
        model = Survey
        fields = ('ordered_maincourse',)

class MainCourseQuestionsForm(forms.ModelForm):

    # This form is question 7, 8 and 9 of the survey

    MAINCOURSE_TIME_CHOICES = [
        ('fast', '10-15 minutes or less'),
        ('normal', '16-21 minutes'),
        ('slow', '22 minutes or more'),
    ]
    time_maincourse = forms.ChoiceField(
        label='How long did it take for your main course to arrive after placing your order or finishing your previous course?',
        choices=MAINCOURSE_TIME_CHOICES,
        widget=forms.RadioSelect
    )
    SIZE_MAINCOURSE_CHOICES = [
        ('Yes', 'Yes'),
        ('Somewhat', 'Somewhat'),
        ('No', 'No'),
    ]
    size_maincourse = forms.ChoiceField(
        label='Would you agree your main course was a generous size',
        choices=SIZE_MAINCOURSE_CHOICES,
        widget=forms.RadioSelect
    )
    PRESENTATION_MAINCOURSE_CHOICES = [
        ('Excellent','Excellent taste and presentation'),
        ('Great', 'Great taste and presentation'),
        ('Somewhat', 'Either the taste or the presentation let the meal down'),
        ('No', 'Both were poor'),
    ]
    presentation_maincourse = forms.ChoiceField(
        label='To what extent did you appreciate the presentation and taste of your main course?',
        choices=PRESENTATION_MAINCOURSE_CHOICES,
        widget=forms.RadioSelect
    )

    class Meta:
        model = Survey
        fields = ('time_maincourse','size_maincourse','presentation_maincourse',)

class VariertyMainCourseForm(forms.ModelForm):

    #This form is question 10 of the survey

    VARIETY_MAINCOURSE_CHOICES = [
        ('Excellent','Excellent variety'),
        ('Great', 'Great variety'),
        ('Somewhat', 'There was some variety'),
        ('No', 'I felt that there was no variety'),
    ]
    variety_maincourse = forms.ChoiceField(
        label='How did you find the variety of the main course menu?',
        choices=VARIETY_MAINCOURSE_CHOICES,
        widget=forms.RadioSelect
    )

    class Meta:
        model = Survey
        fields = ('variety_maincourse',)

class ChooseDessertForm(forms.ModelForm):

    # This form is question 11 of the survey

    ORDERED_DESSERT_CHOICES = [
        ('yes','yes'),
        ('no','no'),
    ]
    ordered_dessert = forms.ChoiceField(
        label='Did you order a dessert?',
        choices=ORDERED_DESSERT_CHOICES,
        widget=forms.RadioSelect
    )

    class Meta:
        model = Survey
        fields = ('ordered_dessert',)

class DessertQuestionsForm(forms.ModelForm):

    #This form is question 12, 13 and 14 of the survey

    DESSERT_TIME_CHOICES = [
        ('fast', '7-11 minutes or less'),
        ('normal', '11-16 minutes'),
        ('slow', '17 minutes or more'),
    ]
    time_dessert = forms.ChoiceField(
        label='How long did it take for your dessert to arrive after placing your order or finishing your previous course?',
        choices=DESSERT_TIME_CHOICES,
        widget=forms.RadioSelect
    )
    SIZE_DESSERT_CHOICES = [
        ('Yes', 'Yes'),
        ('Somewhat', 'Somewhat'),
        ('No', 'No'),
    ]
    size_dessert = forms.ChoiceField(
        label='Would you agree your dessert was a generous size',
        choices=SIZE_DESSERT_CHOICES,
        widget=forms.RadioSelect
    )
    PRESENTATION_DESSERT_CHOICES = [
        ('Excellent','Excellent taste and presentation'),
        ('Great', 'Great taste and presentation'),
        ('Somewhat', 'Either the taste or the presentation let the meal down'),
        ('No', 'Both were poor'),
    ]
    presentation_dessert = forms.ChoiceField(
        label='To what extent did you appreciate the presentation and taste of your dessert?',
        choices=PRESENTATION_DESSERT_CHOICES,
        widget=forms.RadioSelect
    )

    class Meta:
        model = Survey
        fields = ('time_dessert','size_dessert','presentation_dessert',)

class VariertyDessertForm(forms.ModelForm):

    #This form is question 15 of the survey

    VARIETY_DESSERT_CHOICES = [
        ('Excellent','Excellent variety'),
        ('Great', 'Great variety'),
        ('Somewhat', 'There was some variety'),
        ('No', 'I felt that there was no variety'),
    ]
    variety_dessert = forms.ChoiceField(
        label='How did you find the variety of the dessert menu?',
        choices=VARIETY_DESSERT_CHOICES,
        widget=forms.RadioSelect
    )

    class Meta:
        model = Survey
        fields = ('variety_dessert',)

class ChooseDrinkForm(forms.ModelForm):

    # This form is question 16 of the survey

    ORDERED_DRINK_CHOICES = [
        ('yes','yes'),
        ('no','no'),
    ]
    ordered_drink = forms.ChoiceField(
        label='Did you order any drinks with your meal?',
        choices=ORDERED_DRINK_CHOICES,
        widget=forms.RadioSelect
    )

    class Meta:
        model = Survey
        fields = ('ordered_drink',)

class DrinkQuestionsForm(forms.ModelForm):

    # This form is questions 17, 18 and 19 of the survey

    DRINK_TIME_CHOICES = [
        ('fast', '7-11 minutes or less'),
        ('normal', '11-16 minutes'),
        ('slow', '17 minutes or more'),
    ]
    time_drink = forms.ChoiceField(
        label='Roughly how long did it take for your drinks to come once you had placed the order?',
        choices=DRINK_TIME_CHOICES,
        widget=forms.RadioSelect
    )
    SIZE_DRINK_CHOICES = [
        ('Yes', 'Yes'),
        ('Somewhat', 'Somewhat'),
        ('No', 'No'),
    ]
    size_drink = forms.ChoiceField(
        label='Would you agree your dessert was a generous size',
        choices=SIZE_DRINK_CHOICES,
        widget=forms.RadioSelect
    )
    PRESENTATION_DRINK_CHOICES = [
        ('Excellent','Excellent taste and presentation'),
        ('Great', 'Great taste and presentation'),
        ('Somewhat', 'Either the taste or the presentation let the meal down'),
        ('No', 'Both were poor'),
    ]
    presentation_drink = forms.ChoiceField(
        label='To what extent did you appreciate the presentation and taste of your dessert?',
        choices=PRESENTATION_DRINK_CHOICES,
        widget=forms.RadioSelect
    )

    class Meta:
        model = Survey
        fields = ('time_drink','size_drink','presentation_drink',)

class VariertyDrinkForm(forms.ModelForm):

    # This form is question 20 of the survey

    VARIETY_DRINK_CHOICES = [
        ('Excellent','Excellent variety'),
        ('Great', 'Great variety'),
        ('Somewhat', 'There was some variety'),
        ('No', 'I felt that there was no variety'),
    ]
    variety_drink = forms.ChoiceField(
        label='How did you find the variety of the dessert menu?',
        choices=VARIETY_DRINK_CHOICES,
        widget=forms.RadioSelect
    )

    class Meta:
        model = Survey
        fields = ('variety_drink',)

class GreetingEntryForm(forms.ModelForm):

    # This form is question 21 of the survey

    GREETING_CHOICES = [
        ('Excellent','Yes, we had a warm and friendly greeting'),
        ('Great', 'Yes but the we did not feel totally welcomed'),
        ('Somewhat', 'Yes but our greeter was disinterested in us/rude'),
        ('No', 'No one was there to greet us'),
    ]
    greeting_entry = forms.ChoiceField(
        label='Was there someone to greet you upon entry to the restaurant?',
        choices=GREETING_CHOICES,
        widget=forms.RadioSelect
    )

    class Meta:
        model = Survey
        fields = ('greeting_entry',)

class GreetingWaitingForm(forms.ModelForm):

    # This form is question 22 of the survey

    GREETING_WAITING_CHOICES = [
        ('Excellent','No, we got a table straight away'),
        ('Great', 'Yes, but only a short while'),
        ('Somewhat', 'Yes, the wait was noticeable'),
        ('No', 'Yes the wait was very long'),
    ]
    greeting_waiting = forms.ChoiceField(
        label='Did you have to wait for a table?',
        choices=GREETING_WAITING_CHOICES,
        widget=forms.RadioSelect
    )

    class Meta:
        model = Survey
        fields = ('greeting_waiting',)

class GreetingCleanForm(forms.ModelForm):

    # This form is question 23 of the survey

    GREETING_CLEAN_CHOICES = [
        ('Excellent','Yes, our table was clean and had all tableware'),
        ('Great', 'Our table was clean but we were missing some tableware'),
        ('Somewhat', 'Our table was dirty but we had all our tableware'),
        ('No', 'No, our table was dirty and all of our tableware was missing'),
    ]
    greeting_clean = forms.ChoiceField(
        label='Was your table clean when you were seated?',
        choices=GREETING_CLEAN_CHOICES,
        widget=forms.RadioSelect
    )

    class Meta:
        model = Survey
        fields = ('greeting_clean',)

class GreetingOrderForm(forms.ModelForm):

    # This form is question 24 of the survey

    GREETING_ORDER_CHOICES = [
        ('yes','Yes'),
        ('no', 'no'),
        
    ]
    greeting_order = forms.ChoiceField(
        label='Was your order taken promptly once you were ready?',
        choices=GREETING_ORDER_CHOICES,
        widget=forms.RadioSelect
    )

    class Meta:
        model = Survey
        fields = ('greeting_order',)

class UseRestroomForm(forms.ModelForm):

    # This form is question 25 of the survey

    CHOOSE_RESTROOM_CHOICES = [
        ('yes','Yes'),
        ('no', 'no'),
        
    ]
    use_restroom = forms.ChoiceField(
        label='Did you use the restrooms?',
        choices=CHOOSE_RESTROOM_CHOICES,
        widget=forms.RadioSelect
    )

    class Meta:
        model = Survey
        fields = ('use_restroom',)

class RestroomQuestionsForm(forms.ModelForm):

    # This form is question 26 and 27 of the survey

    RESTROOM_CLEAN_CHOICES = [
        ('Excellent','Yes, I could have eaten my dinner off of the toilets'),
        ('Great', 'They were clean with a few exceptions'),
        ('Somewhat', 'They were mostly dirty with a few exceptions'),
        ('No', 'They were totally filthy'),
    ]
    restroom_clean = forms.ChoiceField(
        label='Were the restrooms clean and well maintained?',
        choices=RESTROOM_CLEAN_CHOICES,
        widget=forms.RadioSelect
    )

    CHOOSE_RESTROOM_MISSING_CHOICES = [
        ('yes','Something was missing or something was out of order'),
        ('no', 'Everything was perfect'),
        
    ]
    missing_restroom = forms.ChoiceField(
        label='Was the restroom missing any toilet paper, soap or was anything out of order',
        choices=CHOOSE_RESTROOM_MISSING_CHOICES,
        widget=forms.RadioSelect
    )

    class Meta:
        model = Survey
        fields = ('restroom_clean','missing_restroom',)

class RestaurantCleanForm(forms.ModelForm):

    # This form is question 28 of the survey

    CHOOSE_RESTROOM_CLEAN_CHOICES = [
        ('very bad','I did notice multiple aspects of the restaurant that was dirty or poorly maintained'),
        ('bad', 'I did notice some aspect of the restaurant that was dirty or poorly maintained'),
        ('great', 'No, everything was perfect for our visit'),
        
    ]
    clean_restaurant = forms.ChoiceField(
        label='In any other part of the restaurant inside or out was anything dirty or poorly maintained',
        choices=CHOOSE_RESTROOM_CLEAN_CHOICES,
        widget=forms.RadioSelect
    )

    class Meta:
        model = Survey
        fields = ('clean_restaurant',)

class RestaurantPayBillForm(forms.ModelForm):

    # This form is question 29 of the survey

    PAY_BILL_CHOICES = [
        ('very bad', 'No, The bill was confusing'),
        ('bad', 'No, it was complicated for us to get separate bills'),
        ('great', 'Yes, there was no trouble'),
        
    ]
    pay_bill_restaurant = forms.ChoiceField(
        label='Did you find your bill easy to pay?',
        choices=PAY_BILL_CHOICES,
        widget=forms.RadioSelect
    )

    class Meta:
        model = Survey
        fields = ('pay_bill_restaurant',)

class RestaurantServiceStaffForm(forms.ModelForm):

    # This form is question 30 of the survey

    SERVICE_STAFF_CHOICES = [
        ('excellent','Yes, all three'),
        ('great', 'I found the staff to embody at least two of these qualities'),
        ('poor', 'I found the staff to embody at least one of these qualities'),
        ('bad', 'No, The staff seemed disinterested in me and my group'),
        
    ]
    service_staff = forms.ChoiceField(
        label='During your visit did you find our staff attentive, friendly and helpful?',
        choices=SERVICE_STAFF_CHOICES,
        widget=forms.RadioSelect
    )

    class Meta:
        model = Survey
        fields = ('service_staff',)







