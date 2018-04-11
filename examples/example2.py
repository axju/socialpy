from socialpy.data.post.models import BasicPost



for post in BasicPost.objects.all():
    print(post)
