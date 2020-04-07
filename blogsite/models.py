from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.



class BaseModel(models.Model):
    date_add = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract =True

class Person(BaseModel):
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    profile = models.ImageField(upload_to='userimage')

    def __str__(self):
        return self.name,' profile have been saved'
    



class Category(BaseModel):
    name = models.CharField(max_length=200)

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
    created_by = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name='author')
    slug = models.SlugField()
    tags = TaggableManager()
    total_views = models.PositiveIntegerField(default=0)

    def get_absolute_url(self):
       
        return reverse('blogsite:detail', args=[str(self.slug),str(self.id)])
    


    def __str__(self):
        return '{} > {}'.format(self.subcategory,self.title)




