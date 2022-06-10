from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
# Create your models here.
state_choices = (("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry"))


class Agent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "agentuser" )
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile = models.CharField(max_length=10)
    company_name = models.CharField(max_length=100)
    company_address = models.CharField(max_length=100)
    pincode =models.CharField(max_length=6, default='000000')
    gstin = models.CharField(max_length=100)
    image = models.ImageField(upload_to="")
    gst_state = models.CharField(choices=state_choices,max_length=255)
    country = CountryField(default='India')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "createdby")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "updatedby")

    def __str__(self):
        return str(self.username)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "custuser" )
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile = models.CharField(max_length=10)
    address = models.CharField(max_length=250)
    pincode =models.CharField(max_length=6, default='000000')
    state = models.CharField(choices=state_choices,max_length=255)
    country = CountryField(default='India')
    image = models.ImageField(upload_to="")
    def __str__(self):
        return str(self.username)


class CorporateCust(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "corporateuser" )
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile = models.CharField(max_length=10)
    address = models.CharField(max_length=250)
    pincode =models.CharField(max_length=6,default='000000')
    state = models.CharField(choices=state_choices,max_length=255)
    country = CountryField(default='India')
    image = models.ImageField(upload_to="")
    def __str__(self):
        return str(self.username)