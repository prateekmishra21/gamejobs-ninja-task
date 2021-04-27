from django.db import models
from django.contrib.auth.models import User
# Create your models here.
book_type = [['Physical','Physical'],['Ebook','Ebook']]

class GenreList(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class UserBook(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    genre = models.ForeignKey(GenreList,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=100, null=True)
    type = models.CharField(max_length=100, null=True,choices=book_type)
    review_stars = models.IntegerField(null=True)
    review = models.TextField(null=True)
    favorite = models.BooleanField(default=False)
    bookfile = models.FileField(null=True,blank=True)
    bookcover = models.FileField(null=True,blank=True)

    def __str__(self):
        return self.title
