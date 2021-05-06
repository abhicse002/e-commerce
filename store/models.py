from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'
    # def get_absolute_url(self):
    #     return reverse('store:category_list' , args=[self.slug])
    def __str__(self):
        return  self.name

    def get_absolute_url(self):
        return reverse('store:category_detail', args=[self.slug])

#models is an interface that interacts with our database
#By default, Django adds a Manager with the name objects to every Django model class.
#However, if you want to use objects as a field name, or if you want to use a name other than objects for the Manager, you can rename it on a per-model basis.
#we create this manager class of a Model inorder to make view as thin as possible and Model as fat as possible
class ProductManager(models.Manager):
#Modifying a manager’s initial QuerySet¶
#You can override a Manager’s base QuerySet
    def get_queryset(self):
        return super(ProductManager,self).get_queryset().filter(is_active=True)

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='unknown')
    description = models.TextField(blank=True)
    image= models.ImageField(upload_to='images/')
    slug= models.SlugField(max_length=255,unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    products = ProductManager()

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])



