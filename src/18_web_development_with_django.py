# # Part 18: Web Development with Django
#
# # Install Django: pip install django
#
# # 1. Create a Django Project
# # Run these commands in your terminal or command prompt
# django-admin startproject myproject
# cd myproject
#
# # 2. Create a Django App
# python manage.py startapp myapp
#
# # 3. Define Models, Views, and Templates
# # Edit myapp/models.py
# from django.db import models
#
# class Item(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#
# # Edit myapp/views.py
# from django.shortcuts import render
# from .models import Item
#
# def item_list(request):
#     items = Item.objects.all()
#     return render(request, 'myapp/item_list.html', {'items': items})
#
# # Create myapp/templates/myapp/item_list.html
# # Add HTML code to display the list of items
#
# # 4. Configure URLs
# # Edit myapp/urls.py
# from django.urls import path
# from .views import item_list
#
# urlpatterns = [
#     path('items/', item_list, name='item_list'),
# ]
#
# # Edit myproject/urls.py
# from django.contrib import admin
# from django.urls import path, include
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('myapp.urls')),
# ]
#
# # 5. Run the Development Server
# python manage.py runserver
#
# # Visit http://127.0.0.1:8000/items/ in your web browser
#
# # 6. Create and Apply Migrations
# python manage.py makemigrations
# python manage.py migrate
#
# # 7. Create an Admin User
# python manage.py createsuperuser
#
# # Follow the prompts to create an admin user
#
# # 8. Add Admin Configuration
# # Edit myapp/admin.py
# from django.contrib import admin
# from .models import Item
#
# admin.site.register(Item)
