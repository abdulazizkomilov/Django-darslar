from django.db import models
# from django.contrib.auth.models import User


from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, blank=True)
    avatar = models.ImageField(null=True, blank=True)
    follower = models.ManyToManyField('User', blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []



class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='media')
    # slug =
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.title)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.body)
    

# class Userprofile(models.Model):
#     user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
#     avatar = models.ImageField(upload_to='avatar/')
