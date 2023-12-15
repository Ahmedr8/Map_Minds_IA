
from django.contrib import admin
from django.urls import path
from IA_project import views
urlpatterns = [
    path(r'', views.recommend_destination),
    path('admin/', admin.site.urls),
]
