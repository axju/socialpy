from django.urls import path, include
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from socialpy.server.rest import views

router = routers.DefaultRouter()
router.register(r'category', views.CategoryViewSet)
router.register(r'post', views.PostViewSet)

app_name = 'rest'
urlpatterns = [
    path('', include(router.urls), name='index'),
    path('docs/', include_docs_urls(title='The SocialPy Data-Server API')),
    path('schema/', get_schema_view(title='The SocialPy Data-Server API')),
    path('auth/', include('rest_framework.urls')),
]
