from django import forms
from .models import Blog, AddCourse, Marks


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['Title', 'Content']


class AddCourseForm(forms.ModelForm):
    class Meta:
        model = AddCourse
        fields = ['student', 'course', 'section']


class MarksForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = ['student', 'course', 'marks']