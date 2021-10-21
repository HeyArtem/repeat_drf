from django.urls import path
from blog_app.views import (blog_post_list_create,
                            blog_post_detail
                            )

urlpatterns = [
    path('', blog_post_list_create),
    path('post/<int:pk>/', blog_post_detail)
]
