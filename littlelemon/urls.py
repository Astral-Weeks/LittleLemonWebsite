from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from restaurant import views
from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls.static import serve
from .settings import get_mime_type

import settings

from django.conf.urls.static import static
from .settings import DEBUG

router = routers.DefaultRouter()
# router.register(r'users', views.UsersView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('restaurant.urls')),
    path('', include(router.urls)),
    path('', include('django.contrib.auth.urls')),
    path('auth/users/', views.signup, name='sign-up'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api-token-auth/', obtain_auth_token),
    path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT, 'mime_type': get_mime_type}),
]

if DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)