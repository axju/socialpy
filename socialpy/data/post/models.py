from django.db import models

class BasicPost(models.Model):
    '''only the basic post'''
    text = models.TextField(default='')

    def __str__(self):
        return str(self.id) + ' | '+ self.text[:100]
