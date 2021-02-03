import json

import cloudinary
from django.db.models import Q
from cloudinary.forms import cl_init_js_callbacks
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from nwaben import settings
from .forms import SongForm
from .models import Album, Song
from nwaben.cloudinary_settings import cloudinary_url, cloudinary_upload_preset


class AlbumList(ListView):
    model = Album
    template_name = 'mp3/album_list.html'
    context_object_name = 'albums'

    # def get_queryset(self):
    #     query = self.request.GET.get('q')
    #     album_qs = Album.objects.filter(uploaded_by=self.request.user).filter(
    #         Q(album_name__icontains=query) | Q(artist__icontains=query)
    #     )
    #     return album_qs


class AlbumDetail(DetailView):
    model = Album
    template_name = 'mp3/album_detail.html'

    def get_context_data(self, **kwargs):
        print(self.get_object())
        context = super(AlbumDetail, self).get_context_data(**kwargs)
        context['songs'] = self.get_object().song_set.all().order_by('-song_title')
        context['key'] = settings.RAVE_PUBLIC_KEY
        # a_file = Song.objects.get_or_create(album_token=self.get_object().album_token)
        # context['audio_file_url'] = Song.objects.get()
        return context

    # @csrf_exempt
    # def post(self, *args, **kwargs):
    #     # data = self.request.POST
    #     audio_url = self.request.POST.get(str("audioUrl"))
    #     print(type(audio_url), audio_url)
    #     song_title = self.request.POST.get(str("songTitle"))
    #     print(type(song_title), song_title)
    #     file_inst = Song.objects.create(song_token=self.get_object().album_token,
    #                                     song_title=song_title,
    #                                     audio_file=audio_url)
    #     file_inst.save()
    #     return JsonResponse({'message': 'Audio upload processing...'})


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_name', 'genre', 'album_logo']

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        form.save()
        return super(AlbumCreate, self).form_valid(form)


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_name', 'genre', 'album_logo']


class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('mp3:album_list')


class SongList(ListView):
    model = Song
    context_object_name = 'songs'
    template_name = 'mp3/song_list.html'
    paginate_by = 20

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.album = get_object_or_404(Album, slug=self.kwargs.get('slug'))

    def get_context_data(self, **kwargs):
        context = super(SongList, self).get_context_data(**kwargs)
        context['album'] = self.album
        return context

    def get_queryset(self):
        return self.album.song_set.order_by('-song_title')


class SongCreate(CreateView):
    model = Song

    def get(self, request, *args, **kwargs):
        form = SongForm
        print(self.kwargs)
        return render(request, 'mp3/song_form.html', {'form': form})

    def post(self, request, *args, **kwargs):
        # -------get album instance------
        album_obj = Album.objects.get(slug=self.kwargs.get('slug'))
        if request.method != 'POST':
            form = SongForm()
            return render(request, 'mp3/song_form.html', {'form': form})
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mp3:album_detail', slug=album_obj.slug)


class SongDelete(DeleteView):
    model = Song
    success_url = reverse_lazy('mp3:song_list')
