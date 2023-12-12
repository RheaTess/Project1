from django.shortcuts import render,redirect
from.models import *
from AdminApp.models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
import stripe
from django.conf import settings
stripe.api_key=settings.STRIPE_SECRET_KEY




# Create your views here.
def home(request):
    fiteroptions=Category.objects.all()
    return render(request,'home.html',{'fiteroptions':fiteroptions})

def register(request):
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')

def contact(request):
    fiteroptions=Category.objects.all()
    return render(request,'contact.html',{'fiteroptions':fiteroptions})

def registerdata(request):
    if  request.method=='POST':                                    
        name=request.POST['name']
        email=request.POST['email']
        phno=request.POST['phno']
        password=request.POST['password']
        data=Register(Name=name,Email=email,PhNo=phno,Password=password)
        data.save()
    return redirect('login')

def feedbackdata(request):
    if  request.method=='POST':                                    
        name=request.POST['name']
        phno=request.POST['phno']
        message=request.POST['message']
        data=Feedback(Name=name,PhNo=phno,Message=message)  
        data.save()
    return redirect('home')

def logindata(request):
    if request.method == "POST":

        name=request.POST.get('email')

        password=request.POST.get('password')

        if Register.objects.filter(Email=name,Password=password).exists():

           data = Register.objects.filter(Email=name,Password=password).values('id','Name','PhNo').first()

           request.session['loginname'] = data['Name']

           request.session['loginid'] = data['id']

           request.session['loginpassword'] = password

           request.session['loginemail'] = name  

           request.session['loginphno'] = data['PhNo'] 
           return redirect('home') 

        else:

            return render(request,'login.html',{'msg':'Invalid User Credentials'})

    else:
        return redirect('register')


def logout(request):

    del request.session['loginname']

    del request.session['loginid']
    
    del request.session['loginphno']

    del request.session['loginemail']

    del request.session['loginpassword']
    return redirect('home')

def saloncards(request):
    
    data1=Category.objects.all()
    return render(request,'saloncards.html',{'data1':data1})

    

def details(request,categoryid):
    data=Services.objects.filter(id=categoryid)
    return render(request,'details.html',{'data':data})

def services(request,categoryid):
    if(categoryid =="all"):
        data=Services.objects.all()
    else:
        data=Services.objects.filter(categoryid=categoryid)
    data1=Category.objects.all()
    return render(request,'services.html',{'data':data,'data1':data1})

def bookingform(request):
    userid=request.session.get('loginid')
    bookingformdata=Services.objects.filter(id=userid)
    data=Services.objects.all()
    return render(request,'bookingform.html',{'bookingformdata':bookingformdata, 'data':data})

# def get_date_service(request, serviceid):
#     if request.method == "POST":
#         date = request.POST['date']
#         servicerequired = request.POST['servicerequired']
#         request.session['selected_date'] = date
#         request.session['selected_service'] = servicerequired
#         return redirect(f'/bookingform/{serviceid}')
#     return render(request, "details.html")

def bookingdata(request):
    if  request.method=='POST': 
        userid=request.session.get('loginid')   
        serviceid=request.POST['serviceid']                               
        fname=request.POST['fname']
        lname=request.POST['lname']
        address1=request.POST['address1']
        address2=request.POST['address2']
        address3=request.POST['address3']
        selected_date = request.POST['date']
        request.session['serviceid'] = serviceid
        request.session['fname'] = fname
        request.session['lname'] = lname
        request.session['address1'] = address1
        request.session['address2'] = address2
        request.session['address3'] = address3
        request.session['selected_date'] = selected_date

        
        servicedetails = Services.objects.get(id=serviceid) 
        session = stripe.checkout.Session.create(
            payment_method_types = ['card'],
            line_items=[{
                    'price_data':{
                        'currency': 'inr',
                        'product_data':{
                            'name': servicedetails.Add_Services,
                        },
                        'unit_amount':int(servicedetails.Price)*100,
                    
                    },
                    'quantity':1,
            }],
            mode='payment',
            success_url = "http://127.0.0.1:8000/pay_success?session_id={CHECKOUT_SESSION_ID}",
            cancel_url = "http://127.0.0.1:8000/pay_cancel",
        )
        return redirect(session.url, code=303)

    return redirect('appoinments')

def pay_success(request):
    userid=request.session.get('loginid')   
    serviceid = request.session.get('serviceid')
    fname = request.session.get('fname')
    lname = request.session.get('lname')
    address1 = request.session.get('address1')
    address2 = request.session.get('address2')
    address3 = request.session.get('address3')
    selected_date = request.session.get('selected_date')
    data=BookingForm(userid=Register.objects.get(id=userid),serviceid=Services.objects.get(id=serviceid),FName=fname,LName=lname,Address1=address1,Address2=address2,Address3=address3,Date=selected_date)
    data.save()
    return render(request,'paysuccess.html')

def pay_cancel(request):
    del request.session['serviceid']
    del request.session['fname']
    del request.session['lname']
    del request.session['address1']
    del request.session['address2']
    del request.session['address3']
    return render(request,'paycancel.html')
 

def appoinments(request):
    currentdata=BookingForm.objects.all()
    return render(request,'appoinments.html',{'currentdata':currentdata})



