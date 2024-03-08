from django.db import models

# Create your models here.
class product(models.Model):
    name = models.CharField(max_length = 200)

    
class Cart(models.Model):
    name = models.CharField(max_length = 200)

class Order(models.Model):
    name = models.CharField(max_length = 200)

class process(models.Model):
    name = models.CharField(max_length=200)

class NotNew(models.Model):
    name = models.CharField(max_length=200)

class NotHope(models.Model):
    hope_percentage = models.FloatField()

class Goal(models.Model):
    hope_percentage = models.FloatField()