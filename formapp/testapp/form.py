from django import forms

class EmployeeForm(forms.Form):
    ename = forms.CharField(max_length=100)
    esal = forms.IntegerField()
    add = forms.CharField(max_length=100)