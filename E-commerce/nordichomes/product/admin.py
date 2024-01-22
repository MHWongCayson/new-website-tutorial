from django.contrib import admin
from .models import Category, Product, Book


# allow user to register data using the admin website
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Book)
