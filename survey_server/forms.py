from django import forms

class Question1Form(forms.Form):
    ordered_starter = forms.BooleanField(label='Did you order a starter?', required=True)

class Question2Form(forms.Form):
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


class Question3Form(forms.Form):
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

class Question4Form(forms.Form):
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

class Question5Form(forms.Form):
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




