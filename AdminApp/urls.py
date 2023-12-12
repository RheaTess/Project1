from django.urls import path
from.import views

urlpatterns = [
    path('categoryform',views.categoryform,name='categoryform'),
    path('category',views.category,name='category'),
    path('registerdatatable',views.registerdatatable,name='registerdatatable'),
    path('bookingtable',views.bookingtable,name='bookingtable'),
    path('feedbacktable',views.feedbacktable,name='feedbacktable'),
    path('adminpage',views.adminpage,name='adminpage'),
    path('addservices',views.addservices,name='addservices'),
    path('addservicesform',views.addservicesform,name='addservicesform')
]