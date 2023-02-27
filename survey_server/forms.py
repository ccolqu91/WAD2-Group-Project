from django import forms
from .models import *

class Question1Form(forms.ModelForm):
    ordered_starter_choices = [
        ('yes','yes'),
        ('no','no'),
    ]
    ordered_starter = forms.ChoiceField(
        label='Did you order a starter?',
        choices=ordered_starter_choices,
        widget=forms.RadioSelect
    )

    class Meta:
        model = Survey
        fields = ('ordered_starter',)

class Question2Form(forms.ModelForm):
    STARTER_TIME_CHOICES = [
        ('fast', '7-11 minutes or less'),
        ('normal', '11-16 minutes'),
        ('slow', '17 minutes or more'),
    ]
    starter_time = forms.ChoiceField(
        label='Roughly how long did it take for your starter to come once you had placed the order?',
        choices=STARTER_TIME_CHOICES,
        widget=forms.RadioSelect
    )

    class Meta:
        model = Survey
        fields = ('starter_time',)


class Question3Form(forms.ModelForm):
    SIZE_STARTER_CHOICES = [
        ('Great', 'Great'),
        ('Somewhat', 'Somewhat'),
        ('No', 'No'),
    ]
    size_starter = forms.ChoiceField(
        label='Would you agree your starter was a generous size?',
        choices=SIZE_STARTER_CHOICES,
        widget=forms.RadioSelect
    )

    class Meta:
        model = Survey
        fields = ('size_starter',)

class Question4Form(forms.ModelForm):
    presentation_starter_choices = [
        ('Excellent','Excellent'),
        ('Great', 'Great'),
        ('Somewhat', 'Somewhat'),
        ('No', 'No'),
    ]
    presentation_starter = forms.ChoiceField(
        label='To what extent did you appreciate the presentation and taste of your starter?',
        choices=presentation_starter_choices,
        widget=forms.RadioSelect
    )

    class Meta:
        model = Survey
        fields = ('presentation_starter',)

class Question5Form(forms.ModelForm):
    variety_starter_choices = [
        ('Excellent','Excellent variety'),
        ('Great', 'Great variety'),
        ('Somewhat', 'There was some variety'),
        ('No', 'I felt that there was no variety'),
    ]
    variety_starter = forms.ChoiceField(
        label='How did you find the variety of the starters menu?',
        choices=variety_starter_choices,
        widget=forms.RadioSelect
    )

    class Meta:
        model = Survey
        fields = ('variety_starter',)




