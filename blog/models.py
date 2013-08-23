from django.db import models

# Create your models here.
class Post(models.Model):
	"""docstring for Post"""
	title = models.CharField(max_length=255)
	slug = models.CharField(max_length=255)
	content = models.TextField()
	created_date = models.DateTimeField(auto_now_add=True)

