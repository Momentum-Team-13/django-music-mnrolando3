from django.shortcuts import render, redirect, get_object_or_404
from .models import Album, Artist
from .forms import AlbumForm, TrackForm, ArtistForm


# Create your views here.
def album_list(request):
    albums = Album.objects.all()
    return render(request, "albums/album_list.html",
                  {"albums": albums})


def add_album(request):
    if request.method == 'GET':
        album_form = AlbumForm()
        artist_form = ArtistForm()
    else:
        album_form = AlbumForm(request.POST, request.FILES)
        artist_form = ArtistForm(request.POST)
        if album_form.is_valid() and artist_form.is_valid():
            album_form.save()
            artist_form.save()
            return redirect(to='album_list')
            # else post the data; if form is valid save and return to list

    return render(request, "albums/add_album.html", {"album_form": album_form, "artist_form": artist_form})


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
