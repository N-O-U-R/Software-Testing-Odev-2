from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='blog_images/', null=True)  # Specify a subdirectory for blog images
    content = models.TextField()
    categories = models.CharField(max_length=100, null=True)  # Consider using ManyToManyField for real use
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

