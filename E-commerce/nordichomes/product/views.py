from django.shortcuts import render, get_object_or_404
from .models import Product, Book

def product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product/product.html' , {'product':product})

# when clicked, render the html page and pull the data as context
def book(request):
    book = Book.objects.all()
    return render(request, 'product/book.html', {'book':book })
