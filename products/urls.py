"""
URL configuration for products project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from main.views import products_list_view, ProductDetailsView, ProductFilteredReviews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', products_list_view),
    path('products/<int:product_id>/', ProductDetailsView.as_view()),
    path('products/reviews/<int:product_id>/', ProductFilteredReviews.as_view())
]
