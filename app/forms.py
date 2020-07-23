from django import forms
from django.db import transaction
from .models import Book,User,Student
from django.contrib.auth.forms import UserCreationForm

#form to createbook
class BookCreate(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

#teacher form
class TeacherSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        if commit:
            user.save()
        return user


class StudentSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        return user
