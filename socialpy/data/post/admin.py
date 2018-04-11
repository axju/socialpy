from django.contrib import admin
from django.contrib import auth
from .models import BasicPost

admin.site.unregister(auth.models.User)
admin.site.unregister(auth.models.Group)

admin.site.register(BasicPost)
