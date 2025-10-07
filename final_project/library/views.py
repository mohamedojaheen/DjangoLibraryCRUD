from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import BookForm, AuthorForm
from .models import Book, Author
from django.views.decorators.csrf import csrf_protect

def home(request):
    books = Book.objects.all()
    return render(request, "library/home.html", {"books": books})

def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, "library/book_detail.html", {"book": book})

def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = BookForm()
    return render(request, "library/add_book.html", {"form": form})

@csrf_protect
def reauthenticate(request):
    next_url = request.POST.get("next") or request.GET.get("next", "/")
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            request.session["reauthenticated"] = True
            return redirect(next_url)
        return render(request, "library/reauthenticate.html", {"error": "Invalid credentials", "next": next_url})
    return render(request, "library/reauthenticate.html", {"next": next_url})

@csrf_protect
def add_author(request):
    if request.method == "GET":
        if not request.session.get("reauthenticated", False):
            return redirect(f"/reauthenticate/?next={request.path}")
        form = AuthorForm()
        return render(request, "library/add_author.html", {"form": form})

    if not request.session.get("reauthenticated", False):
        return redirect(f"/reauthenticate/?next={request.path}")

    form = AuthorForm(request.POST)
    if form.is_valid():
        form.save()
        request.session["reauthenticated"] = False
        return redirect("home")

    return render(request, "library/add_author.html", {"form": form})
