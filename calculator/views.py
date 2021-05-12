from django.shortcuts import render, reverse, get_object_or_404
from calculator.forms import CalculateForm
from calculator.models import BmiCalculate, Weight, Height
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')

def dashboard_login(request):
    return render(request,'dashboard_login.html')

def my_records(request):
    forms=BmiCalculate.objects.filter(user="prajuna")
    context={'forms':forms}

    return render(request, 'my_records.html', context)

def calculate_bmi(request):
    form=CalculateForm(request.POST)
    if form.is_valid():   
        user= form.cleaned_data['user']
        wei=form.cleaned_data['weight']
        hei=form.cleaned_data['height']

        print(wei)
        print(hei)
        return HttpResponseRedirect(reverse('calculator:result'))
    context={'form':form}
    return render(request, 'form.html', context)

    # if request.POST:
    #     form = CalculateForm(request.POST)
    #     if form.is_valid():
    #         return HttpResponseRedirect('/')
    # else:
    #     form = CalculateForm()
    # return render(request, 'form.html', {'form': form})
def result(request):
    return render(request, 'result.html')

def save_bmi(request):
    form=CalculateForm(request.POST or None)
    context={"form":form}
    if form.is_valid(): 
        form.save()
        return HttpResponseRedirect("/calculate")
    return render(request, "form.html", context)

def delete_data(request, id):
    data=get_object_or_404(BmiCalculate, id=id)
    data.delete()
    return HttpResponseRedirect(reverse('calculator:records'))