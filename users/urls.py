#Users URLs#

#Django
from django.urls import path
from django.views.generic import TemplateView

#views
from users import views

urlpatterns = [

    #Posts
    path(
        route='usuario/(?P<username>.*)/',
        view=views.AccountView.as_view(),
        name='detail'
    ),

    #Management
    path(
        route='login/',
        view=views.LoginView.as_view(),
        name='login'
    ),
    path(
        route='logout/',
        view=views.LogoutView.as_view(),
        name='logout'
    ),
    path(
        route='signup/',
        view=views.SignupView.as_view(),
        name='signup'
    ),
    path(
        route='me/profile/',
        view=views.UpdateProfile.as_view(),
        name='update_profile'
    ),
    path(
        route='account/',
        view=views.AccountView.as_view(),
        name='account'
    )
]
