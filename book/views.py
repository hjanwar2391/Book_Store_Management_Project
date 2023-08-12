from django.shortcuts import render, redirect
from book.forms import BookStoreForm
from book.models import BookStoreModel

# Create your views here.

def home(request):
    return render(request, 'home.html')

def storebook(request):
    if request.method == 'POST':
        book =  BookStoreForm(request.POST)
        if book.is_valid():
            book.save(commit=True)
            # print(book.changed_data)
            return redirect('showbook')
            
            
    else:
        book =  BookStoreForm()
    return render(request, 'storebook.html',{'form': book})

def showbook(request):
    book = BookStoreModel.objects.all()
    print(book)
    return render(request, 'showbook.html', {'data': book})


def editbook(request, id):
    book = BookStoreModel.objects.get(pk = id)
    form = BookStoreForm(instance = book)
    if request.method == 'POST':
        book =  BookStoreForm(request.POST, instance = book)
        if book.is_valid():
            book.save(commit=True)
            # print(book.changed_data)
            return redirect('showbook')
        
    else:
        book =  BookStoreForm()
    return render(request, 'storebook.html', {'form':form})


def deleteBook(request, id):
    book = BookStoreModel.objects.get(pk = id).delete()
    return redirect(showbook)