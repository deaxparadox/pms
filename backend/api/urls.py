from django.urls import include, path




from . import views
from .views import heading as heading_views

app_name = "api"

urlpatterns = [
    # mounted on the root
    # /api/v1/
    path(
        "", include(
            [
                path("", views.home_view, name="api_home_view"),
                path("<int:id>/", heading_views.GetSingleHeading.as_view(), name="api_single_heading_view"),
            ]
        )
    ),
    # mounted on path
    # /api/v1/
    path(
        "task/",
        include(
            [
                path("", views.tasks_view, name="api_tasks_view"),
                path("<int:id>/", views.get_single_task, name="api_single_tasks_view"),
            ]
        )
    ),
    
    
    
    
    
]