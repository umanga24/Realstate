from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Location(models.Model):
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.location



class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    price = models.IntegerField(default=100)
    image = models.ImageField(upload_to= 'product_photos', null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    Description = models.TextField(max_length=300, null=True)

    def __str__(self):
        return self.name












