from django.shortcuts import render, redirect
from .models import Book,User,Student
from .forms import BookCreate,TeacherSignUpForm,StudentSignUpForm
from django.http import HttpResponse
from django.contrib.auth import login,logout
from django.views.generic import CreateView, ListView, UpdateView
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .decorators import student_required,teacher_required



#DataFlair
def index(request):
    shelf = Book.objects.all()
    return render(request, 'app/library.html', {'shelf': shelf})

def upload(request):
    upload = BookCreate()
    if request.method == 'POST':
        upload = BookCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('books')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'books'}}">reload</a>""")
    else:
        return render(request, 'app/upload_form.html', {'upload_form':upload})


def update_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
        return redirect('books')
    book_form = BookCreate(request.POST or None, instance = book_sel)
    if book_form.is_valid():
       book_form.save()
       return redirect('books')
    return render(request, 'app/upload_form.html', {'upload_form':book_form})
def delete_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
        return redirect('books')
    book_sel.delete()
    return redirect('books')

#home page

class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def home(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            return redirect('books')
        else:
            return redirect('books')
    return render(request, 'app/home.html')

#students

class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')

#teachers

class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')

#logout
@login_required
def user_logout(request):
    logout(request)
    return render(request,'app/home.html',{})
