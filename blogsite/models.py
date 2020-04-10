from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.



class BaseModel(models.Model):
    date_add = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract =True

class CustomUser(AbstractUser):
    # add additional fields in here
    profile = models.ImageField(upload_to='profiles')
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    
class Category(BaseModel):
    name = models.CharField(max_length=200,unique=True)

    def __str__(self):
        return self.name


class Subcategory(BaseModel):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='categories')
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ['-date_updated']
    def __str__(self):
        return '{} > {}'.format(self.category,self.name)
    

class Article(BaseModel):
    subcategory = models.ForeignKey(Subcategory,on_delete=models.CASCADE,related_name='articles')
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to='%d-%m-%Y/images',blank=True, null=True)
    story=RichTextField()
    active = models.BooleanField(default=True)
    created_by = models.ForeignKey(CustomUser,on_delete=models.DO_NOTHING,related_name='author_writings')
    slug = models.SlugField()
    tags = TaggableManager()
    total_views = models.PositiveIntegerField(default=0)
    source =  models.URLField(help_text='source link',blank=True, null=True)

    class Meta:
        ordering = ['-date_updated']

    def get_absolute_url(self):
       
        return reverse('blogsite:detail', args=[str(self.slug),str(self.id)])
    
    def full_name(self):
        return self.created_by.get_full_name()

    def __str__(self):
        return '{} > {}'.format(self.subcategory,self.title)




