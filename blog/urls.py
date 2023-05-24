from django.urls import path
from . import views
from django.db import migrations

# class Migration(migrations.Migration):
#     dependencies = [
#     ]

#     operations = [
#     ]

urlpatterns = [
    path('', views.post_list, name='post_list'),
]