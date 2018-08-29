from socialpy import API_NAMES, POST_STATUS

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    '''only the basic post'''
    status = models.CharField(max_length=10, choices=tuple((name, name) for name in POST_STATUS), default=POST_STATUS[0])
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    categorys = models.ManyToManyField(Category, related_name='posts', blank=True)

    text = models.TextField(default='', blank=True)
    image = models.ImageField(upload_to='image/', blank=True, null=True)

    def __str__(self):
        return str(self.id) + ' | '+ self.text[:100]

class PostOn(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='poston')
    created = models.DateTimeField(auto_now_add=True)
    network = models.CharField(max_length=10, choices=tuple((name, name) for name in API_NAMES))

@receiver(post_save, sender=PostOn)
def publish_post(sender, instance, created, **kwargs):
    if created:
        instance.post.status = 'publish'
        instance.post.save()
