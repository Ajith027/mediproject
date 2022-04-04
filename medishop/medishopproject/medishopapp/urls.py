from django.urls import path

from . import views

app_name='medishop'

urlpatterns = [
    path('',views.index,name='index'),
    path('product/<int:product_id>',views.detail,name='detail'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('alomeds',views.alloitems,name='alloitems'),
    path('homeomeds',views.homeitems,name='homeitems'),
    path('ayurmeds',views.ayuritems,name='ayuritems'),
    path('thank', views.thank, name='thank'),

]