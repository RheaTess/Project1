from django.shortcuts import render,redirect
from.models import *
from user.models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.

def categoryform(request):
    if  request.method=='POST':                                    
        category=request.POST['category']
        image=request.FILES['image'] 
        data=Category(category=category,Image=image)
        data.save()
    return redirect('adminpage')

def category(request):
     categoryFormdata=Category.objects.all()  
     return render(request,'category.html',{'categoryform':categoryFormdata})

def registerdatatable(request):
    tabledata=Register.objects.all()
    totalregistered_users = Register.objects.count()
    return render(request,'registerdata.html',{'registertabledata':tabledata,'totalregistered_users': totalregistered_users})

def feedbacktable(request):
    feedbacktabledata=Feedback.objects.all()
    totalconatcts_users = Feedback.objects.count()
    return render(request,'feedbacktable.html',{'feedbacktabledata':feedbacktabledata,'totalconatcts_users': totalconatcts_users})

def bookingtable(request):
    bookingtabledata=BookingForm.objects.all()
    totalbookings_users = BookingForm.objects.count()
    return render(request,'bookingtable.html',{'bookingtabledata':bookingtabledata,'totalbookings_users': totalbookings_users})

def adminpage(request):
    return render(request,'adminpage.html')


def addservices(request):
    categorydata=Category.objects.all()
    return render(request,'addservices.html',{'categorydata':categorydata})

def addservicesform(request):
    if  request.method=='POST':                                    
        addservices=request.POST['addservices']
        price=request.POST['price']
        image=request.FILES['image']
        categoryname=request.POST['categoryname']
        data=Services(Add_Services=addservices,Price=price,categoryid=categoryname,Image=image)
        data.save()
    return redirect('adminpage')

