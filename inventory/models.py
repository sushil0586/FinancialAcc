
from django.db import models
from django.db.models.deletion import CASCADE
from helpers.models import TrackingModel
from Authentication.models import User

class Product(TrackingModel):
    ProductName = models.CharField(max_length= 255)
    ProductDesc = models.TextField()
    is_stockable = models.BooleanField(default=True)
    owner = models.ForeignKey(to= User, on_delete= models.CASCADE)

    class Meta:
        def __str__(self):
            return self.title
            




