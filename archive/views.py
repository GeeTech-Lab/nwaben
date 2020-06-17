from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from archive.models import Album, Song


class AlbumList(ListView):
    model = Album
    template_name = 'archive/music_list'
    context_object_name = 'all_albums'

    def get_queryset(self):
        query = self.request.GET.get('q')
        album_qs = Album.objects.filter(uploaded_by=self.request.user).filter(
            Q(album_name__icontains=query) | Q(artist__icontains=query)
        )
        return album_qs


class AlbumDetail(DetailView):
    model = Album
    template_name = 'archive/album_detail.html'


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_name', 'genre', 'album_logo']


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_name', 'genre', 'album_logo']


class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('archive:album_list')


class SongList(ListView):
    model = Song
    template_name = 'song_list.html'
    context_object_name = 'songs in this album'

    def get_queryset(self):
        query = self.request.GET.get('q')
        song_qs = Song.objects.all().filter(
            Q(song_title__icontains=query) | Q(album__album_name__icontains=query)
        ).distinct()
        return song_qs


class SongCreate(CreateView):
    model = Song
    fields = ['album', 'song_title', 'audio_file', 'track_number']
    success_url = reverse_lazy('archive:add_song')


class SongDelete(DeleteView):
    model = Song
    success_url = reverse_lazy('archive:song_list')
