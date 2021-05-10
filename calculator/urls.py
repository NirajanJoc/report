from django.urls import path
from calculator.views import dashboard

app_name="calculator"
urlpatterns=[
    path('',dashboard, name='dashboard'),
]