from django.urls import path
from fatch_data import views


urlpatterns = [
    path('login/',views.login_view),
    path('get_profile/',views.get_profile),
]
