from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class login_form(models.Model):
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=25)


class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('title')

class Product_details(models.Model):
    title=models.CharField(max_length=30)
    images=models.ImageField(upload_to="media")
    desc=models.CharField(max_length=60)
    

    objects = models.Manager()
    pets = CustomManager()
    
    class Meta:
        db_table='Pet'

class Birds_details(models.Model):
    title=models.CharField(max_length=30)
    images=models.ImageField(upload_to="media")
    desc=models.CharField(max_length=60)
    

    objects = models.Manager()
    pets = CustomManager()

    class Meta:
        db_table='Birds'

#Cart

class Cart(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )

    cart_id = models.CharField(max_length=250,blank=True)
    pet = models.ForeignKey(Product_details, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total_price = models.FloatField(default=0.00)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='pending')
    notes = models.TextField(blank=True, null=True)

    def _str_(self):
        return f"Cart ID: {self.cart_id}, User: {self.user.username}, Pet: {self.Product_details.name}"

    


    

# #one2one

# class Staff(models.Model):
#     name=models.CharField(max_length=30)
#     age=models.IntegerField()
#     mobile=models.IntegerField()

#     def __str__(self):
#         return str(self.name)

# class Layoff(models.Model):
#     staff_user=models.OneToOneField(Staff, on_delete=models.PROTECT, primary_key=True)
#     language=models.CharField(max_length=20)

#     def __str__(self):
#         return str(self.staff_user)

# #many2one

# class Author(models.Model):
#     name = models.CharField(max_length=30, blank=False, unique=True)
#     age = models.IntegerField(max_length=2)
#     number = models.IntegerField(max_length=10)
#     def __str__(self):
#         return str(self.name)

# class Book(models.Model):
#     author = models.ForeignKey(Author, on_delete=models.PROTECT, blank=False)
#     title = models.CharField(max_length=50)
#     publish_year = models.SmallIntegerField()

#     def __str__(self):
#         return str(self.title)
