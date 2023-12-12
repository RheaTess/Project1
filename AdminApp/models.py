from django.db import models

# Create your models here.
class Category(models.Model):
    category= models.CharField(max_length=255)
    Image=models.ImageField(upload_to='image',default="null.jpg")
    



class Services(models.Model):
    # salonid=models.ForeignKey(Salons,on_delete=models.CASCADE,null=True,blank=True)
    Add_Services=models.CharField(max_length=60)
    Price=models.IntegerField()
    Image=models.ImageField(upload_to='image',default="null.jpg")
    categoryid=models.CharField(max_length=100,default='')
   



    


   
    