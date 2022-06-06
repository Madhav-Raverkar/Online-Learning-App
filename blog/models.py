from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    cname = models.CharField(max_length=30)
    cicon = models.ImageField()
    cdesc = models.CharField(max_length=1000)
    regdate = models.DateField()

    def __str__(self):
        return "%s" % (self.cname)


class Blog(models.Model):
    cname = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    discrption = models.CharField(max_length=1000)
    regdate = models.DateField()

    def __str__(self):
        return self.title + "|" + str(self.author)

class Contact(models.Model):
    uname = models.CharField(max_length=30)
    mobno = models.IntegerField()
    email = models.EmailField()
    udesc = models.CharField(max_length=1000)

    def __str__(self):
        return "%s %s" % (self.uname, self.email)
