from django.db import models

class Post(models.Model):
    post_title = models.CharField(max_length=256)
    post_body = models.TextField()
    post_image = models.CharField(max_length=256)
    publish_date = models.DateTimeField("date published")
    author_id = models.CharField(max_length=256)