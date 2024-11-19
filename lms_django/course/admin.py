from django.contrib import admin
from .models import Category, Course, Lesson, Comment, Quiz

admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Comment)
admin.site.register(Quiz)
