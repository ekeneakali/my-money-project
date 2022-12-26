
from django.db import models

from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField

from djmoney.models.fields import MoneyField

from django_countries.fields import CountryField




# Create your models here.

class Category(models.Model):
    select = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    


    def __str__(self):
        return self.select

    class Meta():
        verbose_name_plural = 'Category'



class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='name of product')
    price = models.IntegerField()
    old = models.IntegerField(blank=True, null=True, verbose_name='old price(optional)')
    created_by = models.CharField(max_length=50)
    image = models.FileField(upload_to='uploads/', verbose_name='upload a photo')
    supply = models.IntegerField(verbose_name='how many days of supply')
    country = models.CharField(verbose_name='your country')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='select business type')
    phone_number = PhoneNumberField()
    email = models.EmailField()
    country = CountryField()
    video= models.FileField(upload_to='uploads/', blank=True, null=True, verbose_name='upload a video(optional)')
    description = models.TextField()
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    favourite = models.ManyToManyField(User, related_name='favourite', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    
    def total_likes(self):
        return self.likes.count()

    class Meta():
        verbose_name_plural = 'Product'





class Profile(models.Model):
    name = models.CharField(max_length=150)
    upload = models.FileField(upload_to='profile_upload')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    


    def __str__(self):
        return self.name

    class Meta():
        verbose_name_plural = 'Profile'



class NewsLetter(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    
    def __str__(self):
        return self.name

    class Meta():
        verbose_name_plural = 'NewsLetter'

class Order(models.Model):
    name = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    email = models.EmailField()
    telephone = models.CharField(max_length=150)
    company = models.CharField(max_length=150)
    address_1 = models.CharField(max_length=150)
    address_2 = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    postcode = models.CharField(max_length=150)
    zone_id = models.CharField(max_length=150)
    country_id = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    


    def __str__(self):
        return self.name

    class Meta():
        verbose_name_plural = 'Order'

class OrderBy(models.Model):
    name = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    email = models.EmailField()
    telephone = models.CharField(max_length=150)
    company = models.CharField(max_length=150)
    address_1 = models.CharField(max_length=150)
    address_2 = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    postcode = models.CharField(max_length=150)
    zone_id = models.CharField(max_length=150)
    country_id = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    


    def __str__(self):
        return self.name

    class Meta():
        verbose_name_plural = 'OrderBy'




class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=700)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name_plural = 'NewsLetter'




class Store(models.Model):
    pst_title = models.CharField(max_length=150, verbose_name='name of product')
    price = models.IntegerField()
    created_by = models.CharField(max_length=50)
    image = models.FileField(upload_to='uploads/', verbose_name='upload a photo')
    supply = models.IntegerField(verbose_name='how many days of supply')
    country = models.CharField(verbose_name='your country')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='select business type')
    phone_number = PhoneNumberField()
    email = models.EmailField()
    country = CountryField()
    video = models.FileField(upload_to='uploads/', blank=True, null=True, verbose_name='upload a video(optional)')
    description = models.TextField()
    likes = models.ManyToManyField(User, related_name='plenty_likes', blank=True)
    favourite = models.ManyToManyField(User, related_name='plenty_favourite', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.pst_title
    
    def total_likes(self):
        return self.likes.count()

    class Meta():
        verbose_name_plural = 'Store'




class Checkout(models.Model):
    first_name = models.CharField(max_length=150)
    created_by = models.CharField(max_length=50, verbose_name='last name')
    phone_number = PhoneNumberField()
    email = models.EmailField()
    address = models.CharField(max_length=1000)
    apartment = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    country = CountryField()
    post_code = models.IntegerField(verbose_name='zip postal code')
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.first_name
    
    
    class Meta():
        verbose_name_plural = 'Checkout'



STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=300, unique=True)
    image = models.FileField(upload_to='blog-image', verbose_name='upload an image')
    created_by = models.CharField(max_length=100, verbose_name='author')
    video = models.FileField(upload_to='blog-video', null=True, blank=True, verbose_name='upload a video(optional)')
    description = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='enough_likes', blank=True)
    favourite = models.ManyToManyField(User, related_name='enough_favourite', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.title
    
    def total_likes(self):
        return self.likes.count()

    
    class Meta():
        verbose_name_plural = 'Post'


class Comment(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    image = models.FileField(upload_to='BLOG-COMMENT-IMAGE', verbose_name='upload personal image')
    comment = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post.title

    class Meta():
        verbose_name_plural = 'Comment'


