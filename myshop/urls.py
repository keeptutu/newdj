from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('details/<int:good_id>/', views.details, name='good_id'),
    path('cart/',views.cart,name='cart'),
    path('<user_id>',views.user_zone,name='user_id')
]