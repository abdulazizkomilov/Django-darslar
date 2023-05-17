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
    like = models.ManyToManyField(User, related_name = 'like', blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)

    #  ---------------------- start new  ------------------------
    favourites = models.ManyToManyField(
        User, related_name='favourite', default=None, blank=True)
    #  ---------------------- end new  ------------------------

    author = models.ForeignKey(User, on_delete=models.CASCADE)
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

    #  ----------------------  new  ------------------------
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    class Meta:
        ordering = ['-updated', '-created']

    
    @property
    def getReplies(self):
        return Comment.objects.filter(parent=self).reverse()
    

    @property
    def is_parent(self):
        if self.parent is None:
            return True

    def __str__(self):
        return self.body
    

