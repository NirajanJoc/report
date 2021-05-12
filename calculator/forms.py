from django import forms
from calculator.models import BmiCalculate
# class CalculateForm(forms.Form):
#     user=forms.CharField()
#     weight=forms.CharField()
#     height=forms.CharField()

class CalculateForm(forms.ModelForm):
    class Meta:
        model=BmiCalculate
        fields="__all__"