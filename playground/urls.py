from django.urls import path
from . import views

# URL config
urlpatterns = [
    path('daily_summary/', views.daily_summary),
    path('tasks/', views.task_list),
    path('settings/', views.test)
]