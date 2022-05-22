from statistics import mode
from unicodedata import name
from django.db import models




class Category(models.Model):

     name= models.CharField(max_length=100)
     description= models.TextField()
     
     def __str__(self):
         return self.name

     
    



class Product(models.Model):
    name= models.CharField(max_length=100)
    description= models.TextField()
    image=models.ImageField()
    price=models.DecimalField(max_digits=11,decimal_places=2)
    category_id=models.ForeignKey(Category,on_delete=models.CASCADE)

    def str(self):
        return self.name


class cart(models.Model):

    name= models.CharField(max_length=100)
    description= models.TextField()
    image=models.ImageField()
    price=models.DecimalField(max_digits=11,decimal_places=2)
    category_id=models.ForeignKey(Category,on_delete=models.CASCADE)

    def str(self):
        return self.name
        
