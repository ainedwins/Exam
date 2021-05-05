from django import forms
from conference.models import Registrationform 

CHOICES = [
    ("Kampala","Kampala"),
    ("Mbarara","Mbarara"),
    ("Jinja","Jinja"),
    ("Nairobi","Nairobi"),
    ("Kabale","Kabale")

]

Category = [
    ("Lecturer","Lecturer"),
    ("Student","Student"),
    ("Speaker","Speaker"),
    ("Researcher","Researcher"),
    ("Job Seeker","Job Seeker"),
    ("Sponsor","Sponsor")

]

class RegistrationForm(forms.ModelForm):
    Firstname           = forms.CharField(widget=forms.TextInput(attrs={ "type":"text", "class":"form-control", "placeholder":"First Name", "id":"fname",  }))
    Lastname            = forms.CharField(widget=forms.TextInput(attrs={"type":"text", "class":"form-control",  "placeholder":"Last Name", "id":"lname",  }))
    Email               = forms.CharField(widget=forms.TextInput(attrs={ "type":"email", "class":"form-control",  "placeholder":"Email", "id":"email",  }))
    Phone               = forms.CharField(widget=forms.TextInput(attrs={  "type":"text", "class":"form-control",  "placeholder": "Phone", "id":"cell" ,}))
    Address            = forms.CharField(widget=forms.TextInput(attrs={  "type":"text", "class":"form-control", "placeholder":"Address", "id":"address" }))
    City               = forms.CharField( widget=forms.Select(choices=CHOICES,attrs={ "class":"form-control", "name":"city" ,"id":"city" }))  #
    category               = forms.CharField(widget=forms.Select(choices=Category,attrs={ "class":"form-control", "name":"category", "id":"category"})) 
    class Meta:
        model =Registrationform
        fields='__all__'
