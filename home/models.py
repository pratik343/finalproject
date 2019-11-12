from django.db import models

class Home(models.Model):
    userid = models.EmailField(max_length=150, blank=True)
    password = models.CharField(max_length=100, blank=True)
    password2 = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.userid
    
