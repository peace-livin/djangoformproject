from django import forms
from django.core.validators import*
class EmployeeForm(forms.Form):
    ename = forms.CharField(max_length=100)
    esal = forms.IntegerField()
    add = forms.CharField(max_length=100)


    def clean(self):
        inputEname = self.cleaned_data.get('ename')
        if len(inputEname)<12:
            raise forms.ValidationError("Name should be atleast 12 characters")
        return inputEname
    
    def clean_esal(self):
        inputEsal = self.cleaned_data.get('esal')
        if inputEsal<10000:
            raise forms.ValidationError("Salary should be atleast 10000")
        return inputEsal
    
    def clean_add(self):
        inputAdd = self.cleaned_data.get('add')
        if len(inputAdd)<10:
            raise forms.ValidationError("Address should be atleast 12 characters")
        return inputAdd