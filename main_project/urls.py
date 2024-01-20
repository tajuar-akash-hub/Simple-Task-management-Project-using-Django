
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name="homepage"),
    path('show_task/', views.show_task,name="show_task"),
    path('task/', include("task.urls")),
    path('category/', include("category.urls")),
]
