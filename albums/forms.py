# Now we need to define a form class for each of our models in forms.py.
# In this file, we must import the forms object from the django module and the Album, Cover and Song classes from the models module.
from django import forms
from .models import Album, Cover, Song

# Then create a class for the form as a child class of the ModelForm class which is in the forms object.
class AlbumForm(forms.ModelForm):
    class Meta:
        # Inside of the nested Meta class, there will be two class variables.
        # The model variable will be equal to the given model's class.
        model = Album
        # The fields variable is a tuple of the names of all of the form fields which should be included in this form.
        fields = ('title', 'musicians')

# The CoverForm and SongForm should also include an exclude variable which is a tuple of form fields to exclude from being required by the form.
# We will exclude the album form field because this will be set using the primary key of the Album rather than by the user.
class CoverForm(forms.ModelForm):
    class Meta:
        model = Cover
        exclude = ('album',) # The , is required to indicate this is a tuple
        fields = ('image',)

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        exclude = ('album',)
        fields = ('title', 'track')