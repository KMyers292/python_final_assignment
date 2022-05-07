# We will import the AbstractUser class which is meant to be used as a parent class for customer user classes.
# We will also import the re module so that we can sanitize data using regular expressions.
import re
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Every premade Django parent model class ueses a method called clean() which is called every time the model is used.
    # This method is used for performing input sanitization and filtering in the model.
    # It can be overwritten to include additional filtering functionality.
    # The AbstractUser class has several preset attributes which are inherited by our custom child class including username, email, first_name, last_name and password.
    # We can add additional filtering to these by overriding the clean() method.
    def clean(self):
        if self.first_name:
            self.first_name = self.first_name.strip()
            self.first_name = re.sub(r"([^a-zA-Z\-.]+)", "", self.first_name)
            self.first_name = self.first_name.lower().title()

        if self.last_name:
            self.last_name = self.last_name.strip()
            self.last_name = re.sub(r"([^a-zA-Z\-.]+)", "", self.last_name)
            self.last_name = self.last_name.lower().title()

    def __str__(self):
        return self.email