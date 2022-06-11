from django.urls import path, include
from .views import PostListCreateView

urlpatterns = [
    path('', PostListCreateView.as_view(), name='hello'),
]