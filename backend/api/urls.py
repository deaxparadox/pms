from django.urls import path


from . import views
from .views import heading as heading_views

app_name = "api"

urlpatterns = [
    # get all headings (defualt home view)
    path("", views.home_view, name="api_home_view"),

    # get all task
    path("task/", views.tasks_view, name="api_tasks_view"),
    
    path("task/<int:id>/", views.get_single_task, name="api_single_tasks_view"),
    
    path("heading/<int:id>/", heading_views.GetSingleHeading.as_view(), name="api_single_heading_view"),
]
