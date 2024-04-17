import uuid
import boto3
import os

from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from .models import Vinyl, Genre, Photo
from .forms import SongsForm

# All views
def home(request):
    vinyls = Vinyl.objects.all()
    genres = Genre.objects.all()
    vinyl = [vinyls[0], vinyls[1], vinyls[2], vinyls[3]]
    # display only the first 4 album covers, i could have done this with a function, this was my quick fix.
    
    return render(request, 'home.html', {
        'vinyls': vinyl,
        'genres': genres
    })

def about(request):
    return render(request, 'about.html')

def vinyls_index(request):
    vinyls = Vinyl.objects.all()
    return render(request, 'vinyls/index.html', {
        'vinyls': vinyls
    })

def vinyls_detail(request, vinyl_id):
    vinyl = Vinyl.objects.get(id=vinyl_id)
    songs_form = SongsForm()
    id_list = vinyl.genres.all().values_list('id')
    non_genres = Genre.objects.exclude(id__in=id_list)
    genre_list = Genre.objects.all()
    print(vinyl.songs_set.all)
    return render(request, 'vinyls/detail.html', {
        'vinyl': vinyl, 'songs_form': songs_form, 'genres': non_genres, 'genre_list': genre_list
    })

def add_song(request, vinyl_id):
    form = SongsForm(request.POST)
    if form.is_valid():
        new_song = form.save(commit=False)
        new_song.vinyl_id = vinyl_id
        new_song.save()
        
    return redirect('detail', vinyl_id)

def assoc_genre(request, vinyl_id, genre_id):
    Vinyl.objects.get(id=vinyl_id).genres.add(genre_id)
    return redirect('detail', vinyl_id=vinyl_id)

def add_photo(request, vinyl_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            # build the full url string
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            Photo.objects.create(url=url, vinyl_id=vinyl_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('detail', vinyl_id=vinyl_id)

    
# Classes for vinyls
class VinylCreate(CreateView):
    model = Vinyl
    fields = '__all__'
    success_url = '/vinyls'

class VinylsUpdate(UpdateView):
    model = Vinyl
    fields = ['name', 'artist', 'release_year']

class VinylDelete(DeleteView):
    model = Vinyl
    success_url = '/vinyls'


# Classes for genres
class GenreList(ListView):
    model = Genre

class GenreDetail(DetailView):
    model = Genre

class GenreCreate(CreateView):
    model = Genre
    fields = '__all__'
    success_url = '/genres/create'

class GenreDelete(DeleteView):
    model = Genre
    success_url = '/genres'