"""musiciansproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# As with the hello world app, we need to define URLS in our project's urls.py file and use the include() function to point those URLS to our apps.
from django.urls import include, path
# By default, Django's development server can not display uploaded media files.
# Because of this you must add some code to your project app's urls.py file to allow the development server to do so.
# This code should be removed for production.
# This will require the following modules.
from django.conf import settings
from django.conf.urls.static import static
# We need to import the TemplateView class.
# Normally we would use this type of class in our views.py file.
# However, if we don't need to display or alter a model in a aview or if we are simply using one of Django's premade view classes then we can also use the view class directly in our urls.py file.
from django.views.generic.base import TemplateView

# We need to define a URL in our project's urls.py file for our albums.
urlpatterns = [
    path('', TemplateView.as_view(template_name='musiciansproject/templates/welcome.html.django'), name='welcome'),
    # Next we will need to point to our users app the same way we did with the musicians and albums.
    path('users/', include('users.urls')),
    # We also need to create a second path which uses the same address as the previous users path but which access the django.contrib.auth.urls module instead.
    path('users/', include('django.contrib.auth.urls')),
    # This adds Django's premade user registration URLs onto the users/ address.
    path('musicians/', include('musicians.urls')),
    path('albums/', include('albums.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# At the end of the urlpatterns variable, add the static function which references MEDIA_URL and MEDIA_ROOT variables which we will define in the settings.py file later as arguments.
