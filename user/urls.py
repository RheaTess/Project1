from django.urls import path
from.import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('contact',views.contact,name='contact'),
    path('registerdata',views.registerdata,name='registerdata'),
    path('feedbackdata',views.feedbackdata,name='feedbackdata'),
    path('logindata',views.logindata,name='logindata'),
    path('logout',views.logout,name='logout'),
    path('saloncards',views.saloncards,name='saloncards'),
    path('details/<int:categoryid>/',views.details,name='details'),
    path('saloncards',views.saloncards,name='saloncards'),
    path('bookingform',views.bookingform,name='bookingform'),
    path('bookingdata',views.bookingdata,name='bookingdata'),
    path('appoinments',views.appoinments,name='appoinments'),
    path('pay_success',views.pay_success,name='pay_success'),
    path('pay_cancel',views.pay_cancel,name='pay_cancel'),
    # path('get_date_service/<int:serviceid>/',views.get_date_service,name='get_date_service'),
    path('services/<str:categoryid>/',views.services,name='services'),


]