from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.


class Post(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    # i think it sets the author as some sort of author, and on delete just deletes everything under it
    # post has 1 author, authro has many posts probably>?
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self): # get the time zone published
        self.published_date = timezone.now()
        self.save()

    def __str__(self): # i think should allow a string with max len 200 to be printed
        return self.title 
    
