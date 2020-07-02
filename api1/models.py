from django.db import models

# Create your models here.

class Banks(models.Model):
    name= models.CharField(max_length=250)
    id =  models.AutoField(primary_key=100)
    class Meta:
        db_table = 'banks'


class Branches(models.Model):
    ifsc = models.CharField(primary_key=11,max_length=11)
    bank = models.ForeignKey('api1.Banks',on_delete=models.CASCADE)
    branch = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=1000)
    district = models.CharField(max_length=1000)
    state = models.CharField(max_length=1000)

    class Meta:
        db_table = "branches"



    




