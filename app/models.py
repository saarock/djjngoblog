from django.db import models

# Create your models here.


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    fullName = models.CharField(max_length=255)
    email = models.EmailField()
    comment = models.CharField(max_length=1000)
    blogid = models.IntegerField()
    post_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.fullName} - {self.post_date}"



class Contact_us(models.Model):
    id = models.AutoField(primary_key=True)
    fullName = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    message = models.CharField(max_length=1000)
    post_date = models.DateTimeField(auto_now=True)


