from django.db import models
#from django_pandas.managers import DataFrameManager


class Receive_Google_Data(models.Model) :
    key1 = models.IntegerField(default=0)
    G_Word = models.CharField(max_length=200)
    G_Rating = models.IntegerField(default=0) 

 #   objects = DataFrameManager()
    
    def publish(self):
        self.save()
        
    def __str__(self):
        return self.G_Word


class Receive_Naver_Data(models.Model):
    key1 = models.IntegerField(default=0)
    N_Word = models.CharField(max_length=200)
    N_Rating = models.IntegerField(default=0)

#    objects = DataFrameManager()

    def publish(self):
        self.save()

    def __str__(self):
        return self.N_Word

