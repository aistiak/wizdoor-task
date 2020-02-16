from django.db import models

# Create your models here.

class User(models.Model):
    email      = models.CharField(max_length=200)
    cell       = models.CharField(max_length=11,null=True)

    def __str__(self):
        return self.email

class Customer(models.Model):
    user       = models.OneToOneField(User,on_delete=models.CASCADE)
    name       = models.CharField(max_length=200,null=True)    
    location   = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name 
    

class Category(models.Model):
    title = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.title

class Product(models.Model): 
    name        = models.CharField(max_length=200,null=True)
    description = models.CharField(max_length=500,null=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name 

    # def __str__(self):
    #     return self.name

class Order(models.Model):
    customer   = models.ForeignKey(Customer,on_delete=models.CASCADE,default=0) 
    products   = models.ManyToManyField(Product)

    def __str__(self):
        return self.id

