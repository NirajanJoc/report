from django.urls import path
from user_account.views import signin_view, signup_view
app_name='user'
urlpatterns=[
    path('login/',signin_view, name='login'),
    path('signup/',signup_view, name='register'),
]