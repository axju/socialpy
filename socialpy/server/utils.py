from django.contrib.auth.models import User
from django.contrib import auth
from django.utils.deprecation import MiddlewareMixin 

class AutomaticLoginUserMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated: return

        try:
            User.objects.create_superuser('admin', 'admin@example.com', 'admin')
        except:
            pass

        user = auth.authenticate(username='admin', password='admin')
        if user:
            request.user = user
            auth.login(request, user)
