from django.shortcuts import render, redirect, get_object_or_404
from .models import Album, Artist
from .forms import AlbumForm, TrackForm


# Create your views here.
def album_list(request):
    albums = Album.objects.all()
    return render(request, "albums/album_list.html",
                  {"albums": albums})


# Susan's code
def add_album(request):
    if request.method == 'GET':
        form = AlbumForm()
    else:
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            album = form.save(commit=False)
            artist_list = Artist.objects.filter(name=album.add_artist_name)
            if artist_list:
                album.artist = artist_list[0]
            else:
                new_artist = Artist()
                new_artist.name = album.add_artist_name
                new_artist.save()
                album.artist = new_artist
            album.save()
            return redirect(to='album_list')
            # else post the data; if form is valid save and return to list

    return render(request, "albums/add_album.html", {"form": form})


# def add_album(request):
#     if request.method == 'GET':
#         form = AlbumForm()
#     else:
#         form = AlbumForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect(to='album_list')

#     return render(request, "albums/add_album.html", {"form": form})


# def album_detail(request, pk):
#     album = get_object_or_404(Album, pk=pk)
#     return render(request, "albums/album_detail.html", {"album": album})


def edit_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'GET':
        form = AlbumForm(instance=album)
    else:
        form = AlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect(to='album_detail', pk=pk)

    return render(request, "albums/edit_album.html", {"form": form,
                  "album": album})


def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect(to='album_list')

    return render(request, "albums/delete_album.html",
                  {"album": album})


def add_track(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'GET':
        form = TrackForm()
    else:
        form = TrackForm(data=request.POST)
        if form.is_valid():
            new_track = form.save(commit=False)
            new_track.album = album
            new_track.save()
            return redirect(to='album_detail', pk=pk)

    return render(request, "albums/album_detail.html", {"form": form,
                  "album": album})


# def delete_track(request, pk):
#     track = get_object_or_404(Track, pk=pk)
#     album_pk = track.album.pk
#     if request.method == "POST":
#         track.delete()
#         return redirect(to='album_detail', pk=album_pk)


def artist_detail(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    return render(request, "albums/artist_detail.html", {"artist": artist})
