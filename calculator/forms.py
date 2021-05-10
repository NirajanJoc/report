from django import forms

class CalculateForm(forms.Form):
    user=forms.CharField()
    weight=forms.CharField()
    height=forms.CharField()