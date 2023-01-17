from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now
        self.save()
        

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('post_detail', args=[str(self.id)])


        
        