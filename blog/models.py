from email.policy import default
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


    # look for onl published post in the post
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


    # look for only approved posts with true attribute
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)


# for Commenting 
class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.TextField(max_length=50)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)


    # method to approve a comment
    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

