from django import forms
from .models import *
class student_form(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(),required=True,max_length=50)
    emailid = forms.EmailField(widget=forms.EmailInput(),required=True)
    address = forms.CharField(widget=forms.TextInput(),required=False,max_length=50)
    marks = forms.CharField(widget=forms.NumberInput(),required=True,max_length=10)

    class Meta():
        model=student
        fields=['name','emailid','address','marks']



