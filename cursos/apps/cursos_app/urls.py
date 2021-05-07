from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('courses', views.courses, name="courses"),
    path('courses/add', views.add_course, name="add_course"),
    path('/courses/<int:id>/show', views.show_course, name="show_course"),
    path('/courses/<int:id>/delete', views.delete_course, name="delete_course"),
    path('/courses/<int:id>/destroy', views.destroy, name="destroy"),
    path('/courses/comments/add',views.add_comment, name="add_comment"),
]