from django.shortcuts import render
from .models import Libro
from .forms import PostForm

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

# Create your views here.
def book_list(request):
    return render(request, 'biblioteca/book_list.html', {})

def new_book(request):
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
        else:
            form = PostForm()
        return render(request, 'biblioteca/book_edit.html', {'form': form})
