from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField()
    def __str__(self):
        return self.name

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=30)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    slug = models.SlugField()
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="media")
    def __str__(self):
        return self.name

