from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 500, default = None, 
    blank = True, null = True)
    priority = models.IntegerField(default = 0,)

    def __str__(self):
        if self.name:
            return self.name
        else:
            return 'no name specified' 
    

class CategoryImage(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    imgsrc = models.ImageField(upload_to = 'static/images/categories')