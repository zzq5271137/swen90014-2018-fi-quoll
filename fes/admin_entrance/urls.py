from django.contrib.auth import views as auth_view
from django.urls import path

"""
Url for authentication

with xx.xx.xx.xxLport for the default login url
     xx.xx.xx.xx:port/logout/ for the logout url
"""
urlpatterns = [
    path('', auth_view.login, name='login'),

    path('logout/', auth_view.logout, name='logout'),
]
