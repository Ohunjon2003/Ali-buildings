from django.db import models

# Create your models here.

class Area(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)



class Qurilish_tashkiloti(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    when_organized_found = models.CharField(max_length=50,verbose_name='qachon_tashkil_topgan')
    area = models.ForeignKey(Area,on_delete=models.CASCADE)


class Qurilish_binosi(models.Model):
    qurilish_tashkiloti = models.ForeignKey(Qurilish_tashkiloti,on_delete=models.CASCADE)
    area = models.ForeignKey(Area,on_delete=models.CASCADE)
    field = models.CharField(max_length=100,null=True,blank=True,verbose_name='maydoni')
    floor = models.IntegerField(default=0,verbose_name='qavat')
    parking_lot = models.BooleanField(default=True,verbose_name='parkovka')
    playground = models.BooleanField(verbose_name="o'yin maydonchasi")
    lift = models.BooleanField()




