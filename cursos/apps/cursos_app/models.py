from __future__ import unicode_literals
from django.db import models

class CourseManager(models.Manager):
    def validator(self, postData):
        errors = {}

        if(len(postData['name'])) < 5:
            errors['name'] = 'El nombre del curso debe tener a lo menos 6 carateres' 
        
        if(len(postData['description']))<15:
            errors['description'] = 'La descripción debe tener a lo menos 15 caracteres'
        
        return errors
    
class Course(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CourseManager()

class Description(models.Model):
    description = models.CharField(max_length=255)
    course = models.OneToOneField(Course, primary_key=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

class Comment(models.Model):
    comment = models.CharField(max_length=255)
    course = models.ForeignKey(Course, related_name="comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
