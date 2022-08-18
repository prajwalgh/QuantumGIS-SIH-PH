from django.db import models

# Create your models here.
class form1Detail(models.Model):
    Dialer_Name=models.CharField(max_length=300)
    Dialer_Address=models.TextField(max_length=500)
    Describe_call=models.TextField(max_length=500)
    Incident_Type=models.CharField(max_length=500)
    Phone_Number=models.CharField(max_length=20)
    Division=models.CharField(max_length=500)
    District=models.CharField(max_length=500)
    Incident_Address=models.TextField(max_length=500)
    frv_req=models.CharField(max_length=100)
    date = models.DateField()

class FRV(models.Model):
    FRV_Type=models.CharField(max_length=20)
    #FRV_Plate_No=models.CharField(max_length=10)
    Driver_Name=models.CharField(max_length=100)
    #Driver_Number=models.CharField(max_length=20)
    lat=models.CharField(max_length=50)
    lng=models.CharField(max_length=50)
    end_lat=models.CharField(max_length=50)
    end_lng=models.CharField(max_length=50)

class Operations(models.Model):
    id=models.BigIntegerField(primary_key=True)
    Dialer_Name=models.CharField(max_length=300)
    Dialer_Address=models.TextField(max_length=500)
    Describe_call=models.TextField(max_length=500)
    Incident_Type=models.CharField(max_length=500)
    Phone_Number=models.CharField(max_length=20)
    Division=models.CharField(max_length=500)
    District=models.CharField(max_length=500)
    Incident_Address=models.TextField(max_length=500)
    frvs=models.ManyToManyField(FRV, blank=True)
    date = models.DateField()

class History(models.Model):
    id=models.BigIntegerField(primary_key=True)
    Dialer_Name=models.CharField(max_length=300)
    Dialer_Address=models.TextField(max_length=500)
    Describe_call=models.TextField(max_length=500)
    Incident_Type=models.CharField(max_length=500)
    Phone_Number=models.CharField(max_length=20)
    Division=models.CharField(max_length=500)
    District=models.CharField(max_length=500)
    Incident_Address=models.TextField(max_length=500)
    frvs=models.ManyToManyField(FRV, blank=True)
    date = models.DateField()

# class Cases(models.Model):
#     Driver_Name = models.CharField(max_length=300)
#     Dialer_Start_lng = models.TextField(max_length=500)
#     Dialer_Start_lat = models.TextField(max_length=500)
#     Dialer_end_lng = models.TextField(max_length=500)
#     Dialer_end_lat = models.TextField(max_length=500)



