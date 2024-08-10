from django.urls import path
from .views import*

app_name = "common"


urlpatterns = [
    path("", Home.as_view(), name='home'),
    path("blog-single/<str:slug>/", BlogDetails.as_view(), name='blog-single'),
    path("add_comment/<int:blog_id>/", AddComment.as_view(), name='blog-comment'),
    path("contact/", ContactView.as_view(), name="contact"),
]
