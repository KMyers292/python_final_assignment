from django.urls import path
# We also need to define subordinate URLS in our app's urls.py file which will point to specific functions in our views moduke.
# To do this, we need to import the views.py module.
from . import functionviews
# We need at least four URLS, one for each part of the CRUD cycle.
# We can optionally include two URLS which serve the purpose of reading data, one for listing all musicians in the database and one for displaying the data of one musician in detail.

# The detail, edit, and delete URLs need to pass the primary key of the musician in the URL.
# We can do this using the code <int:pk> inside of a path.

urlpatterns = [
    path('', functionviews.index, name='home'), # /musicians
    path('<int:pk>', functionviews.detail, name='detail'), # /musicians/1
    path('add', functionviews.add, name='add'), # /musicians/add
    path('edit/<int:pk>', functionviews.edit, name='edit'), # /musicians/edit/2
    path('delete/<int:pk>', functionviews.delete, name='delete'), # /musicians/delete/3
]