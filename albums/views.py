from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import AlbumForm, CoverForm, SongForm
from .models import Album, Cover, Song

# Create your views here.

class AlbumList(ListView):
    model = Album
    template_name = 'album-index.html.django'
    context_object_name = 'albums'

class AlbumDetail(DetailView):
    model = Album
    template_name = 'album-detail.html.django'
    context_object_name = 'album'

class AlbumCreate(CreateView):
    model = Album
    template_name = 'add-album.html.django'
    fields = AlbumForm.Meta.fields
    success_url = reverse_lazy('albums-home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AlbumCreate, self).form_valid(form)

class AlbumUpdate(UpdateView):
    model = Album
    template_name = 'edit-album.html.django'
    fields = AlbumForm.Meta.fields
    success_url = reverse_lazy('albums-home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AlbumUpdate, self).form_valid(form)

class AlbumDelete(DeleteView):
    model = Album
    template_name = 'delete-album.html.django'
    success_url = reverse_lazy('albums-home')

class CoverCreate(CreateView):
    model = Cover
    template_name = 'add-cover.html.django'
    fields = CoverForm.Meta.fields
    success_url = reverse_lazy('albums-home')

    # We also need to override a method called form_valud to set the foreign key of the Cover to the primary key of the Album which we have passed through the URL.
    # We will do so by setting the album_id attribute of the instance attribute of the form to the primary key.
    # We will retrieve it using the get() method of the kwargs (key word arguments in the form of a dictionary) attribute of this view class.
    def form_valid(self, form):
        form.instance.album_id = self.kwargs.get('pk')
        return super(CoverCreate, self).form_valid(form)
        # Then we will access the super() function to access th parent class.
        # In the super() function we will use the current class name, CoverCreate, as the first argument.
        # We are doing this to take advantage of Python's version of "multiple inheritance" which allows a child class or object to inherit the attributes nad methods of multiple classes.
        # So far, we have only looked at "single inheritance" in Python, but we can pasas a class name into the super() function for that class' attributes and methods to be inherited by object as well.
        # Because the super() function represents an object of the parent class, by default it willonly have access to the attributes and methods of the parent class.
        # By using multiple inheritance we can give th super() function access to the attributes and methods of both the parent CreateView class and the child CoverCreate class.
        # In this case, when the form_valid() method is called on the super() function, it will also have access to any attributes or methods defined in both the CreateView class and the CoverCreate class.

# The SongCreate class will use the same code with the class names switched.
class SongCreate(CreateView):
    model = Song
    template_name = 'add-song.html.django'
    fields = SongForm.Meta.fields
    success_url = reverse_lazy('albums-home')

    def form_valid(self, form):
        form.instance.album_id = self.kwargs.get('pk')
        return super(SongCreate, self).form_valid(form)