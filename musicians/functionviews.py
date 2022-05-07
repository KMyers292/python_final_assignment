# First it is necessary to import the render() and redirect() functions from the django.shortcuts module.
from django.shortcuts import render, redirect
# It is also necessary to import the MusicianForm class from our forms module and the Musician class from our model module.
from .forms import MusicianForm
from .models import Musician

# For the home page function, use the all() method to collect all of the musicians from the database.
# Then return a Django template called index.html.django and pass the musicians to the template as a variable.
def index(request):
    musicians = Musician.objects.all();
    return render(request, 'index.html.django', {
        'musicians': musicians
    })

# To display the data of one specific musician in detail, it is necessary to select that specific musician using the primary key which is passed to the view through <int:pk> in the URL (you can also use <int:id> to get the id column but pk stands for primary key and collects the column which is the primary key which may not nececssarily be the id column). Then you would simply return the corresponding Django template and pass the musician to the template as a variable.
def detail(request, pk):
    musician = Musician.objects.get(pk=pk)
    return render(request, 'detail.html.django', {
        'musician': musician
    })

# For the add function, check to ensure that the request method is using the POST method and if it is not then load the add page with the MusicianForm class which has been passed to the template. If it is using the POST method then create new instance of the MuscianForm class with the data from the POST method as the argument. Check to see if the form is valud and then save the form data if it is. Finally redirect back to the home page.
def add(request):
    if request.method == 'POST':
        form = MusicianForm(request.POST)

        if form.is_valid():
            form.save()

        return redirect('home')
    else:
        form = MusicianForm
        return render(request, 'add.html.django', {
            'form': form
        })

# The edit function works very similarly to the add function.
# The difference is that it is necessary to select the musician we are editing from the database using the primary key.
# Then that instance of a Musician from the database is used as argument to fill out them form fields in the edit page.
# If the request is using the POST method it will redirect back to the edit page.
# If it is not it will load the edit tempalte and pass both the musician and the form as variables to the template.
def edit(request, pk):
    musician = Musician.objects.get(pk=pk)

    if request.method == 'POST':
        form = MusicianForm(request.POST, instance=musician)

        if form.is_valid():
            form.save()

        return redirect('home')
    else:
        form = MusicianForm(instance=musician)
        return render(request, 'edit.html.django', {
            'musician': musician,
            'form': form
        })

def delete(request, pk):
    musician = Musician.objects.get(pk=pk)

    if request.method == 'POST':
        musician.delete()

        return redirect('home')
    else:
        return render(request, 'delete.html.django', {
            'musician': musician
        })




