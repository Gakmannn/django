"""
URL configuration for metanit project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path, include
from hello import views

product_patterns = [
    path("new", views.new),
    path("top", views.top),
]

urlpatterns = [
    path('', views.index, name='home'),
    path('json', views.json),
    re_path(r'^1/.+/?$', views.i2, name='home2'),
    # path('1/<str:name>', views.i2, name='home2'),
    re_path(r'^2/(?P<slug>\d+)?/?$', views.i22,),
    re_path(r'^1/?$', views.i1, name='home1'),
    path("product", views.products),
    path("product/", include(product_patterns)),
    path('admin/', admin.site.urls),
]
