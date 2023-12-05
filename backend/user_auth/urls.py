from django.urls import path, re_path, include



from .views import authenticate_user, create_user, login_user

app_name = "user_auth"


urlpatterns = [
    path(
        "", 
        authenticate_user, 
        name="api_get_authenticated_user"
    ),
    path(
        "login/",
        login_user,
        # include("rest_framework.urls"),
        name="api_get_authenticated_user"
    ),
    path(
        "signup/",
        create_user,
        name="api_create_user"
    )
]
