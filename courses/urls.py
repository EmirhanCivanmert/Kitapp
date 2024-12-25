from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('search', views.search, name="search"),
    path('create-book', views.create_book, name="create_book"),
    path('book-list', views.book_list, name="book_list"),
    path('book-edit/<int:id>', views.book_edit, name="book_edit"),
    path('book-delete/<int:id>', views.book_delete, name="book_delete"),
    path('upload', views.upload, name="upload_image"),
    path('<slug:slug>', views.details, name="book_details"),
    path('kategori/<slug:slug>', views.getCoursesByCategory, name='courses_by_category'),
]
