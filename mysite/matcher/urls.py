from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('review/<int:match_id>/', views.review_match, name='review match'),
]


