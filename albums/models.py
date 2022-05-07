# First we need to import the datetime module which we will use later and the models object from the django.db module.
import re
from django.contrib.auth import get_user_model
from django.db import models
# We also need to import our Musician model.
from musicians.models import Musician

# Create your models here.

# Then create a class to represent an Album.
# This class will be a child class of the Model class which is stored in the models object.
# Then we will create a class variable for an album title.
class Album(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='albums')
    # We will create a relationship between our Album model to our Musician model.
    musicians = models.ManyToManyField(Musician, blank=True, related_name='albums')
    # Each album could have many musicians and each musician could have many albums so we are using a many to many relationship.
    # For many to many relationships, Django uses the ManyToManyField() method.
    # We should set blank to True so that it does not require the musicians attribute to have a value set for it when the user submits the form in order for the form to submit.
    # The related_name parameter is used to set a name which we can use to reference the model in our Django templates.

    def clean(self):
        if self.title:
            self.title = self.title.strip()
            self.title = re.sub(r"([^a-zA-Z0-9\-. ]+)", "", self.title)
            self.title = self.title.lower().title()

    # The __str__() method is used to return a string which in Django is used to identify our model by a label in forms and user interfaces.
    # Adding [:50] restricts the label to the first 50 characters of the name.
    def __str__(self):
        return self.title[:50]

# Next we will create a second model in the same file which will represent an album Cover.
# This model will have two variables.
# The first uses Django's OneToOneField() method to store the primary key of the album which it shares a relationship with.
# Most albums would only have one cover so this makes sense for a one-to-one relationship.
# The first argument of this method is the name of the model which this model shares a relationship with, which in this case is Album.
# We should also set the on_delete parameter to models.CASCADE which indicates that if the album is deleted, the related cover should also be deleted.
# For a one-to-one relationship we would frequently want to make the primary key of the parent model equal to the primary key of the child model using primary_key=TRue.
# For any relational fields, we should also set a related_name which we can use to reference the model in Django templates.
class Cover(models.Model):
    album = models.OneToOneField(Album, on_delete=models.CASCADE, primary_key=True, related_name='cover')
    image = models.ImageField(upload_to='albums/covers/%Y/%m/%d/')

    # The second variable will use an ImageField() method which will allow users to upload their own images for album covers.
    # We will set the upload_to parameter to uplaod the files in a directory which matches the name of our app and then a directory which mataches the type of media.
    # We will also store them in folders which correspond with today's date using the datetime object to keep them more organized.
    # In order to use the ImageField() method it is necessary to install a third-party PIP package called Pillow which is used for image uploads.
    # Unlike FileField(), ImageField() checks to ensure that any uploaded files are image file types.

    def __str__(self):
        return self.image

# We will create a model which represents a Song.
# Every album would have many songs, so we will use a one-to-many relationship.
# Django's ForeignKey() method is used to create one-to-many relationships.
# Like OneToOneField(), this method taks the name of the model which it is related to as the first argument, should be set to deleted if the parent model is deleted using one_delete=modles.CASCADE and should have a related_name.
# However, we would not want the foreign key to be equal to the primary key of this model.
class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs')
    title = models.CharField(max_length=255)
    # The FileField() method is almost the same as the ImageField() method but it can be used with any type and does not require a third-party library.
    # However, it does not check to ensure that the appropriate file type has been uploaded without the addition of another third-party library or code.
    track = models.FileField(upload_to='albums/songs/%Y/%m/%d/')

    def clean(self):
        if self.title:
            self.title = self.title.strip()
            self.title = re.sub(r"([^a-zA-Z0-9\-. ]+)", "", self.title)
            self.title = self.title.lower().title()

    def __str__(self):
        return self.title[:50]