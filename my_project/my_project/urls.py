from django.conf.urls import url
from django.contrib import admin
from app_comments import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^addcomment/', views.addcomment),
]
