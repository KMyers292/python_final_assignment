# First we will need to import Django's premade view classes.
# We will import the ListView class which is designed to list all of the items in a database and the DetailView class which is designed to select one item from a database and display it.
from django.views.generic import ListView, DetailView
# Classes which are used to create, update or delete data need to imported from the edit sub-module of the django.views.generic module.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Then it is necessary to import the reverse_lazy() function.
# This function will redirect to a page but will only do so once a process such as creating or deleting a database entry has been completed.
from django.urls import reverse_lazy
# It is also necessary to import the MusicianForm class from our forms module and the Musician class from our models module.
from .forms import MusicianForm
from .models import Musician

# This class should be a child class of the ListView class.
# Then we need to overwrite the class vsariables of the ListView class to the specific values necessary for this view.
class MusicianList(ListView):
    # Set the model variable to the Musician class to specify which model we want to list out in this view.
    model = Musician
    # Set the template_name to the name of corresponding Django template which you want displayed.
    template_name = 'index.html.django'
    # Finally set the context_object_name variable to the name of the variable you want to use to access and loop through the list of data from the database.
    context_object_name = 'musicians'

# This class should be a child class of the DetailView class.
class MusicianDetail(DetailView):
    model = Musician
    template_name = 'detail.html.django'
    context_object_name = 'musician'

# This class should be a child class of the CreateView class.
# In order to associate our musicians with a specific user we also need to add some code to our MuscianCreate and MusicianUpdate views.
class MusicianCreate(CreateView):
    model = Musician
    template_name = 'add.html.django'
    # Set the fields variable to Muscian.Meta.fields to specify that you want all form fields which are associated with this model to be used in the creation of this data.
    fields = MusicianForm.Meta.fields
    # Finally set the success_url variable to the reverse_lazy() function to indicate what URL the user should be redirected to once the data has finished being created and pass the value of the name argument which we set for the corresponding path() function for the URL in the urls.py file as an argument.
    success_url = reverse_lazy('home')

    # To set the user field to the current user we need to override the preset form_valid() method and set the form.instance.user to self.request.user
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(MusicianCreate, self).form_valid(form)

class MusicianUpdate(UpdateView):
    model = Musician
    template_name = 'edit.html.django'
    fields = MusicianForm.Meta.fields
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(MusicianUpdate, self).form_valid(form)

class MusicianDelete(DeleteView):
    model = Musician
    template_name = 'delete.html.django'
    success_url = reverse_lazy('home')
