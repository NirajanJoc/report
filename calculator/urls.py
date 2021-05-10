from django.urls import path
from calculator.views import dashboard,my_records,calculate_bmi, save_bmi,result

app_name="calculator"
urlpatterns=[
    path('',dashboard, name='dashboard'),
    path('my-records/',my_records, name='records'),
    path('calculate-bmi/',calculate_bmi, name='calculate_bmi'),
    path('save-bmi', save_bmi, name='save_bmi'),
    path('result', result, name='result'),
]