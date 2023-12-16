"""
URL configuration for RudeTrade project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

from userauth.views import *
from addtrade.views import *
from trades.views import *
from dashboard.views import *
from calender.views import *

# from trades.urls import path, include
from django.urls import path



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name='index_name'),
    path('account',views.account, name='account'),
    path('delete_all_trades',views.delete_all_trades, name='delete_all_trades'),
    path('note',views.note, name='note'),

    path('calender',calender, name='calender'),
    path('get_trades_for_date/<str:date>/', get_trades_for_date, name='get_trades_for_date'),

    
    path('dashboard',dashboard, name='dashboard'),
    
    path('trades',trades, name='trades'),

    path('addtrade',addtrade, name='addtrade'),
    path('addtrade-multiple',addtrade_multiple, name='addtrade_multiple'),
    path('newtrade',newtrade, name='newtrade'),
    path('one_more',one_more, name='one-more'),
    path('upload_excel',upload_excel, name='upload_excel'),


    path('signupaction',signupaction),
    path('loginaction',loginaction),
    path('updateuserdetails',views.updateuserdetails),
]
