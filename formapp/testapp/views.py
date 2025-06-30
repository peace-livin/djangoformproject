from django.shortcuts import render
from testapp.form import EmployeeForm

# Create your views here.
def form(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            print("Name is :",form.cleaned_data['ename'])
            print("Salary is :",form.cleaned_data['esal'])
            print("Address is :",form.cleaned_data['add'])
            return render(request,'testapp/form.html',{'form':form})
    return render(request,'testapp/form.html',{'form':form})