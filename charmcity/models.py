from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 200) 
    
    
    def __str__(self):
        return self.name
    



class Sub_category(models.Model):
    name = models.CharField(max_length= 200)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    
    
    def __str__(self):
      return f'{self.name}-- {self.category}'
  
  
  
  
  
class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    weight = models.DecimalField(max_digits = 10 , decimal_places=2)
    size = models.DecimalField(max_digits = 10 , decimal_places = 2)
    price = models.DecimalField(max_digits =10 , decimal_places =2)
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    sub_category = models.ForeignKey(Sub_category, on_delete=models.CASCADE)
    img = models.ImageField(upload_to=' product-img/' )
    sale = models.BooleanField(default = False)
    
    
    def __str__(self):
        return self.name
    
    
    
    
    
class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)   
    user = models.ForeignKey(User, on_delete = models.CASCADE)   
    quantity = models.IntegerField()   
    sub_total = models.DecimalField(max_digits =10 , decimal_places = 2)   
    
    
       
    
    
class Order(models.Model):
    first_name = models.CharField(max_length = 200 )
    last_name = models.CharField(max_length = 200 )
    address = models.CharField(max_length = 200 )
    city = models.IntegerField()
    phone  = models.IntegerField()
    postal = models.IntegerField()
    is_delivered  = models.BooleanField(default = False )

        
    
    
      