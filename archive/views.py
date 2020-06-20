from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from archive.models import Album, Song


class AlbumList(ListView):
    model = Album
    template_name = 'archive/album_list.html'
    context_object_name = 'albums'

    # def get_queryset(self):
    #     query = self.request.GET.get('q')
    #     album_qs = Album.objects.filter(uploaded_by=self.request.user).filter(
    #         Q(album_name__icontains=query) | Q(artist__icontains=query)
    #     )
    #     return album_qs


class AlbumDetail(DetailView):
    model = Album
    template_name = 'archive/album_detail.html'


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_name', 'genre', 'price', 'album_logo']

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        form.save()
        return super(AlbumCreate, self).form_valid(form)


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_name', 'genre', 'album_logo']


class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('archives:album_list')


class SongList(View):
    def get(self, filter_by='track_number'):
        if not self.request.user.is_authenticated:
            return render(self.request, 'account/login.html')
        else:
            try:
                song_ids = []
                for album in Album.objects.filter(user=self.request.user):
                    for song in album.song_set.all():
                        song_ids.append(song.slug)
                users_songs = Song.objects.filter(slug__in=song_ids)
            except Album.DoesNotExist:
                users_songs = []
            return render(self.request, 'archive/song_list.html', {
                'song_list': users_songs,
                'filter_by': filter_by,
            })

    # def get_queryset(self):
    #     query = self.request.GET.get('q')
    #     song_qs = Song.objects.all().filter(
    #         Q(song_title__icontains=query) | Q(album__album_name__icontains=query)
    #     ).distinct()
    #     return song_qs


class SongCreate(CreateView):
    model = Song
    fields = ['album', 'song_title', 'audio_file', 'track_number']
    success_url = reverse_lazy('archives:song_list')


class SongDelete(DeleteView):
    model = Song
    success_url = reverse_lazy('archives:song_list')
