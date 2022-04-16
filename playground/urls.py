from django.urls import path
from django.views.generic.base import RedirectView
from . import views

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

# URL config
urlpatterns = [
    path('daily_summary/', views.DailySummary.as_view()),
    #path('tasks/', views.task_list),
    path('settings/', views.Settings.as_view()),
    path('bargraph/', views.BarGraph.as_view()),
    path('columnchart/', views.ColumnChart.as_view()),
    re_path(r'^favicon\.ico$', favicon_view)
]
