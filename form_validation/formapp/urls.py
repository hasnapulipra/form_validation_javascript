from django.urls import path
from . import views
urlpatterns=[
    path('fun1',views.signup,name='signupform'),
    path('fun2',views.login,name='loginpage'),
    path('fun3',views.home,name='homepage'),

]