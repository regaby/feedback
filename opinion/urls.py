from django.urls import path
from . import views

urlpatterns = [
    path("", views.OpinionView.as_view()),
    path('gracias', views.Gracias.as_view()),
    path('opiniones', views.OpinionListView.as_view()),
    path('opinion/favorito', views.AgregarFavoritoView.as_view()),
    path('opinion/<int:pk>', views.OpinionDetalleView.as_view()),
]
