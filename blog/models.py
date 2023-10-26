from django.db import models
from tinymce.models import HTMLField

class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    Github=models.CharField(max_length=500)
    author=models.CharField(max_length=100)
    slug=models.CharField(max_length=130)
    timeStamp=models.DateTimeField(blank=True)
    category = models.CharField(max_length=59, default="")
    subcategory = models.CharField(max_length=57, default="")
    image = models.FileField(upload_to='post/images/', default="")
    overview=models.TextField()
    post_desc=HTMLField(default="0")
    
    def __str__(self):
        return self.title
 