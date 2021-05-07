from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Course, Description, Comment
from django.urls import reverse

def index(request):
    return redirect('/courses')

def courses(request):
    context = {
        'list': Description.objects.all()
    }
    return render(request, "index.html", context)

def add_course(request):
    Course.objects.create(name=request.POST.get('name'))
    Description.objects.create(description=request.POST.get('description'))

    return redirect('/courses')

def show_course(request, id):
    context = {
        'course': Description.objects.get(course_id=id),
        'comments' : Comment.objects.filter(course_id=id)
    }
    return render(request, "comments.html", context)

def delete_course(request, id):
    context = {
        'course': Description.objects.get(course_id=id)
    }
    return render(request, "delete.html", context)

def destroy(request, id):
    course = Description.objects.get(course_id=id)
    course.delete()
    return redirect('courses')

def add_comment(request):
    course = Course.objects.get(id=request.POST.get('course_id'))
    Comment.objects.create(comment=request.POST.get('comment'),course=course)
    return redirect('show_course', id=request.POST.get('course_id'))