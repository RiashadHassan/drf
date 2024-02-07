from django.db import models

class StreamPlatform(models.Model):
    name = models.CharField(max_length=30)
    about= models.TextField(max_length=500)
    website = models.URLField(max_length=200)
    
    def __str___(self):
        return self.name

class WatchList(models.Model):
    title = models.CharField(max_length=50)
    storyline = models.TextField(max_length=200)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title