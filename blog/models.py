from django.db import models

# Create your models here.
class post(models.Model):
    title=models.CharField(max_length=200)
    body = models.TextField()
    # images=models.ImageField() 
    author=models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
    body=models.TextField(default='')

    def __str__(self):
        return self.title
    