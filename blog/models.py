from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField()    
    publish_date = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.title
    