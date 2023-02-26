from django import forms

class Question1Form(forms.Form):
    ordered_starter = forms.BooleanField(label='Did you order a starter?', required=False)
