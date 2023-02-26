from django import forms

class Question1Form(forms.Form):
    ordered_starter = forms.BooleanField(label='Did you order a starter?', required=True)

class Question2Form(forms.Form):
    time_starter = forms.BooleanField(label='How long did you wait for your starter?', required=False)

class Question3Form(forms.Form):
    variety_starter = forms.BooleanField(label='How was the variety of starters menu?', required=False)

