from django.db import models

class Category(models.Model):
    haha = models.CharField(max_length=100)
    xixi = models.CharField(max_length=100,default='SOME STRING')

    def __str__(self):
        return self.haha