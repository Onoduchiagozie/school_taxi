from django.db import models

class Record(models.Model):
    name=models.CharField(max_length=100,default='')
    pickup_id=models.CharField(max_length=100,default='')
    drop_id=models.CharField(max_length=100,default='')
    price=models.CharField(max_length=100,default='')
    distance=models.CharField(max_length=100,default='')
    date_time=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
