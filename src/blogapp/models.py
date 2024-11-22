from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.TextField(max_length=100)
    description=models.TextField(max_length=300)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to='blog_images/')

    class Meta:
        db_table='blogs'
