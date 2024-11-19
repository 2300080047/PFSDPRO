from django import forms
from .models import Task
from .models import StudentList
from .models import ContactManager


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']


class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentList
        fields = ['Register_Number', 'Name']


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactManager
        fields = ['name', 'email', 'phoneNumber', 'address']

