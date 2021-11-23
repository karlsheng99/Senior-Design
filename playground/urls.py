from django.urls import path
from . import views

# URL config
urlpatterns = [
    path('daily_summary/', views.DailySummary.as_view()),
    #path('tasks/', views.task_list),
    path('settings/', views.Settings.as_view()),
    path('bargraph/', views.BarGraph.as_view())
]
