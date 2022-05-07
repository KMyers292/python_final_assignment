# Similarly to what we did when we used Flask, when collecting user data using forms, it is necessary to define classes for forms using a file called forms.py.
# In this file, we must import the forms object from the django module and the Musician class from the models module.

from django import forms
from .models import Musician

# Then create the class for the form as a child class of the ModelForm class which is in the forms object.
class MusicianForm(forms.ModelForm):
    # It is also possible in Python to create nested classes.
    # Django uses a nested class called Meta for creating forms.
    # This class controls information about the outer class.
    class Meta:
        # Inside of this class, there will be two class variables.
        # The first will be called model and it will be equal to the Musician class.
        model = Musician
        # The second class variable will be called fields and is a tuple of the names of all of the form fields which should be included in this form.
        fields = ('name', 'image', 'genres', 'deceased')

# These fields should match ones which were specified in our model class but we can leave out any fields which we don't want included in the form.