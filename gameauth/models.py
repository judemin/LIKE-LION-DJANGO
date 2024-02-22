from djongo import models


# Create your models here.
class Users(models.Model):
    _id = models.ObjectIdField()
    name = models.TextField(null=False)
    email = models.TextField(null=False, unique=True)
    password = models.TextField(null=False)
    bestScore = models.IntegerField()
