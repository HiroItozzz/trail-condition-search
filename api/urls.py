from django.urls import path

from . import views

urlpatterns = [
    path("api/trail-conditions/", views.ListView.as_view(), name="list"),
    path("api/<int:pk>", views.ListView.as_view(), name="detail"),
    # path("api/areas/{area}/conditions/"),
    # path("api/sources/"),
    # path("api/sources/{id}/conditions/"),
]
