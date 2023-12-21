from django.urls import path
from . import views

urlpatterns=[
  path('' , views.index, name="index"),
  path('login' , views.login , name="login"),
  path('register',views.register, name="register"),
  path('user', views.user, name='user'),
  path('investplans', views.investplans, name='investplans'),
  path('withdrawal', views.withdrawal, name='withdrawal'),
  path('history', views.history, name="history"),
  path('deposit', views.deposit, name="deposit"),
  path('account', views.account, name="account"),
  path('widthdrawhistory', views.widthdrawhistory, name="widthdrawhistory"),
  path('investp', views.investp, name="investp"),
  path('logout', views.logout, name="logout"),
  path('easypay' , views.easypay, name="easypay")
]