from django.urls import path
from library import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path("book/<int:pk>/", views.book_detail, name="book_detail"),
    path("add_book/", views.add_book, name="add_book"),
    path("add_author/", views.add_author, name="add_author"),
    path("reauthenticate/", views.reauthenticate, name="reauthenticate"),
]
