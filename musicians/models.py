# We need to make some changes to our Musician model to allow users to add musicians which are associated with their accounts.
# To do so, we need to import the get_user_model()  function from the django.contrib.auth module.
# This function rereives the user model regardless of whether we are using Django's prset user model or if we are using a custom model.
import re
from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

# Now that we are connected to a database we can create our models.
# First, we need to import the models object from the django.db module.
# Then create a class to represent a Musician.
# This class will be a child class of the Model class which is stored in the models objet.

class Musician(models.Model):
    # Then we will create a class variable to represent each column in the database table for this model.
    # Each variable will use a class which is stored in the models models object that corresponds with the data type of that column.
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='musicians/img/%Y/%m/%d')
    genres = models.TextField()
    deceased = models.BooleanField()
    # We will create a new field in the Musician model called user and will set this to a ForeignKey().
    # Instead of setting the first argument to a hardcoded class we will set it to the get_user_model() function which will reteive the user model class.
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='musicians')

    def clean(self):
        if self.name:
            self.name = self.name.strip()
            self.name = re.sub(r"([^a-zA-Z0-9\-. ]+)", "", self.name)
            self.name = self.name.lower().title()

    # In order for our musicians to display correctly in the Add Labum form, it is necessary to define a method called __str__().
    # This method is used to return a string which is used to identify our model by a label in forms and user interfaces.
    # Adding [:50] restricts the label to the first 50 characters of the name.
    def __str__(self):
        return self.name[:50]

