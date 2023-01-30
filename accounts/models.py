from django.db import models

# Create your models here.

class Product(models.Model):
    GATEGORY = (
        ("Indoor", "Indoor"),
        ("Outdoor", "Outdoor"),
    )

    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    tag = models.ManyToManyField("Tag")
    describe = models.TextField(null=True, blank=True)
    gategory = models.CharField(max_length= 200, choices= GATEGORY, null = True)

    def __str__(self):
        return self.name



class Customer(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, blank= True)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = (
        ("Pending", "Pending"),
        ("Out for Delivery", "Out for Delivery"),
        ("Delivered", "Delivered"),
    )
    status = models.CharField(max_length=200, choices=STATUS)
    customer = models.ForeignKey(Customer, on_delete= models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add= True, null = True)

    def __str__(self):
        return "order of " + self.customer.name


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name