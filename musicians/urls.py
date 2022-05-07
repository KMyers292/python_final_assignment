from django.urls import path
# Now that we have redefined our views as classes we need to redefine URLS in our app's urls.py file and use the as_view() method to point those URLs to the classes we made in our views module.
# To do this we need to import the classes from the views.py module.
from .views import MusicianList, MusicianDetail, MusicianCreate, MusicianUpdate, MusicianDelete

# We need at least four URLS, one for each part of the CRUD cycle.
# We can optionally include two URLS which serve the purpose of reading data, one for listing all musicians in the database and one for displaying the data of one musician in detail.

# The detail, edit, and delete URLs need to pass the primary key of the musician in the URL.
# We can do this using the code <int:pk> inside of a path.

urlpatterns = [
    path('', MusicianList.as_view(), name='home'), # /musicians
    path('<int:pk>', MusicianDetail.as_view(), name='detail'), # /musicians/1
    path('add', MusicianCreate.as_view(), name='add'), # /musicians/add
    path('edit/<int:pk>', MusicianUpdate.as_view(), name='edit'), # /musicians/edit/2
    path('delete/<int:pk>', MusicianDelete.as_view(), name='delete'), # /musicians/delete/3
]