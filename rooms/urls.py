from rest_framework.urls import path
from . import views

urlpatterns = [
    path("amenities/", views.Amenities.as_view()),
    path("amenity/<int:pk>", views.AmenityDetail.as_view()),
]
