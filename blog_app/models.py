from django.db import models
from django.conf import settings
from django.urls import reverse

class Blog_post(models.Model):
    title = models.CharField(max_length=188)
    text = models.TextField()
    author = models.ForeignKey(  settings.AUTH_USER_MODEL , on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('blog_test')