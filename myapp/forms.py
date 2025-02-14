from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    Applying_For = forms.CharField(max_length=100)
    Periods= forms.IntegerField(widget=forms.Textarea)
    Affiliation = forms.CharField(max_length=100)
    Course_and_Subject= forms.CharField(max_length=100)
    From= forms.DateField()
    To= forms.DateField()