from django.urls import path
from . import views
from dlabspro.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('books/',views.index, name='books'),
    path('upload/', views.upload, name = 'upload-book'),
    path('books/update/<int:book_id>', views.update_book),
    path('books/delete/<int:book_id>', views.delete_book),
]

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)