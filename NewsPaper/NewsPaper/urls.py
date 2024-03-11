"""
URL configuration for NewsPaper project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from rest_framework import routers
from news import views


router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'authors', views.AuthorViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'news', views.NewsViewSet)
router.register(r'articles', views.ArticlesViewSet)
router.register(r'comments', views.CommentViewSet)



urlpatterns = [
   path('i18n/', include('django.conf.urls.i18n')),
   path('admin/', admin.site.urls),
   path('pages/', include('django.contrib.flatpages.urls')),
   path("accounts/", include("allauth.urls")),  # Оставили только allauth
   path('news/', include('news.urls')),
   path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
   path('api/', include(router.urls)),
   #path('api-own', include(api.urls)),
   path('swagger-ui/', TemplateView.as_view(
      template_name='swagger-ui.html',
      extra_context={'schema_url':'openapi_schema'}), name='swagger-ui'),
]

# urlpatterns += i18n_patterns(
#    path('', include('basic.urls'))
# )