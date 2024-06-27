from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

class Contract(models.Model):
    full_name=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)
    email=models.EmailField()
    message=models.TextField()


class About(models.Model):
    objects=True
    title=models.CharField(max_length=100)
    content=RichTextField()


class Service(models.Model):
    title=models.CharField(max_length=200)
    content=RichTextField()
    slug=models.SlugField(max_length=200,blank=True,editable=False) # blank bu hisse bos qala biler demekdir

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        super(Service, self).save(*args, **kwargs)


class Slider(models.Model):
    title=models.CharField(max_length=200)
    #  python -m pip install Pillow   kitabxasini yukle
    image=models.ImageField(upload_to='slider/') #upload_to='slider/' slider adli faylda SAXLAYIR SEKILLERI


class Category(models.Model):
    name=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200,unique=True,blank=True,editable=False)# editable=False bu hissenin admin panelde gorsenmemisini temin edir

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.name)
        super(Category,self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='blog/')
    content=RichTextField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    views=models.IntegerField(default=0)
    slug=models.SlugField(max_length=200,unique=True,blank=True,editable=False) # unique eyni bir seyin ikici defe tekrar olunmasinin qarsini alir
    created_at=models.DateTimeField(auto_now_add=True)# auto_now_add vaxti qeyd edir
    updated_at=models.DateTimeField(auto_now=True)#auto_now deyisiklikleri qeyd edir
    tags=TaggableManager()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        super(Blog,self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Setting(models.Model):
    logo_1=models.ImageField(upload_to='dimg/',null=True,blank=True)
    logo_2 = models.ImageField(upload_to='dimg/', null=True, blank=True)
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=255)
    keywords=models.CharField(max_length=255)
    phone_fixed=models.CharField(max_length=15)
    phone_mobile=models.CharField(max_length=15)
    fax=models.CharField(max_length=15)
    email=models.EmailField()
    city=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    address=models.TextField()
    postal_code=models.CharField(max_length=10)
    facebook_url=models.URLField(max_length=255)
    twitter_url = models.URLField(max_length=255)
    instagram_url = models.URLField(max_length=255)
    youtube_url = models.URLField(max_length=255)


class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.blog}'
