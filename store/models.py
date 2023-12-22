from django.db import models
from django.utils import timezone

class Register(models.Model):
    full_name = models.CharField(max_length=255)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=128)  # Hashed password field
    # Add other fields you need for your user model
    # ...

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('prefer_not_to_say', 'Prefer not to say'),
    ]
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    date = models.DateTimeField('date', default=timezone.now())

    # Define any other methods or properties for your user model
def __str__(self):
    return f"Full Name: {self.full_name}, Username: {self.username}, Email: {self.email}, Phone Number: {self.phone_number}, Gender: {self.get_gender_display()}"

class Contact(models.Model):
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField('date', default=timezone.now())

    def __str__(self):
        return f"From: {self.name}, Email: {self.email}, Company: {self.company}"



class Product(models.Model):
    product_name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
	# date = models.DateTimeField('date', default=timezone.now())


    def __str__(self):
        return f"Product: {self.product_name}, Description: {self.description}, Price: {self.price}, Date: {self.date}"
