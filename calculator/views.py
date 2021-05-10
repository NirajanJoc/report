from django.shortcuts import render
from calculator.forms import CalculateForm
# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')


def my_records(request):
    return render(request, 'my_records.html')

def calculate_bmi(request):
    form=CalculateForm(request.POST or None)
    context={'form':form}
    return render(request, 'form.html', context)

def result(request):
    return render(request, 'result.html')

def save_bmi(request):
    pass