from django.shortcuts import render, redirect, get_object_or_404
from .models import Album
from .forms import AlbumForm


# Create your views here.
def album_list(request):
    albums = Album.objects.all()
    return render(request, "albums/album_list.html",
                  {"albums": albums})


def add_album(request):
    if request.method == 'GET':
        form = AlbumForm()
        # if add_contact is requested, the form should be the ContactForm
    else:
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(to='album_list')
            # else post the data; if form is valid save and return to list

    return render(request, "albums/add_album.html", {"form": form})


def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, "albums/album_detail.html", {"album": album})


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

    return render(request, "Albums/delete_Album.html",
                  {"album": album})
