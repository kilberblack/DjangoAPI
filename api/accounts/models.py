from django.db import models

class userProfile(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField()   

    def __str__(self):
        return self.username