
from django.contrib import admin
from django.urls import path,include
app_name='articles'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/',include("articles.urls"))
]
