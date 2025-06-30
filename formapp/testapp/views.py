from django.shortcuts import render
from testapp.form import EmployeeForm

# Create your views here.
def form_view(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
           print("name is : ",form.cleaned_data['ename'])
           print("salary is : ",form.cleaned_data['esal'])
           print("address is : ",form.cleaned_data['add'])
    return render(request,'testapp/form.html',{'form':form})

