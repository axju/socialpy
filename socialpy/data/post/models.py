from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    '''only the basic post'''
    POST_STATUS = (
        ('new', 'New'),
        ('released', 'Released'),
        ('arcive', 'Arcive'),
    )
    status = models.CharField(max_length=10, choices=POST_STATUS, default='new')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    categorys = models.ManyToManyField(Category, related_name='posts', blank=True)

    text = models.TextField(default='')
    image = models.ImageField(upload_to='image/', blank=True, null=True)

    def __str__(self):
        return str(self.id) + ' | '+ self.text[:100]

class PostOn(models.Model):
    NETWORKS = (
        ('facebook', 'facebook'),
        ('twitter', 'Twitter'),
        ('instagram', 'Instagram'),
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='poston')
    created = models.DateTimeField(auto_now_add=True)
    network = models.CharField(max_length=10, choices=NETWORKS)
