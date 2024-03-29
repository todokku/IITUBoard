from django.urls import path

from .views import BoardView, LoginView

app_name = "board"

urlpatterns = [
    path('board/', BoardView.as_view()),
    path('login/', LoginView.as_view()),
]
