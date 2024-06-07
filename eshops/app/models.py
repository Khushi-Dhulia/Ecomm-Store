from django.db import models

# Create your models here.
# class Category(models.Model):
#     name=models.CharField(max_length=100, unique = True)

#     def __str__(self):
#         return self.name
    
class Product(models.Model):
    img=models.ImageField(upload_to='products/')
    name=models.CharField(max_length=100)
    amt=models.IntegerField(default=0)
    # category=models.ForeignKey(Category,on_delete=models.CASCADE,default=True,null=False, related_name='product')
    is_published=models.BooleanField(default=False)
    men = models.BooleanField(default=False)
    women = models.BooleanField(default=False)
    bag = models.BooleanField(default=False)
    watch = models.BooleanField(default=False)
    shoes = models.BooleanField(default=False)
    def __str__(self):
        return self.name

    