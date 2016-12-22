from django.db import models
from django.core.urlresolvers import  reverse
from django import forms

# Create your models here.
class Designers(models.Model):
    designerID=models.CharField(max_length=13,default="des000")
    name=models.CharField(max_length=200)
    firmName=models.CharField(max_length=300)
    contact=models.CharField(max_length=10)
    img=models.FileField()
    point=models.IntegerField(default=100)
    password=models.CharField(max_length=25,default="abc")

    def get_absolute_url(self):
        return reverse('home')



    def __str__(self):
        return "name="+ self.name +" firmname"+self.firmName


class Designers_pro(models.Model):
    designer=models.ForeignKey(Designers,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    firmName = models.CharField(max_length=300)
    contact = models.CharField(max_length=10)
    email = models.EmailField(max_length=300)
    minMarketRate = models.FloatField()
    maxMarketRate = models.FloatField()
    designShare = models.FloatField()
    execShare = models.FloatField()


    def __str__(self):
        return "name="+ self.name +" firmname"+self.firmName+" email"+self.email




