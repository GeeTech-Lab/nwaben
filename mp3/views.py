from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from accounts.models import User
from mp3 import paystack
from nwaben import settings
from .forms import SongForm
from .models import Album, Song


class AlbumList(ListView):
    model = Album
    template_name = 'mp3/album_list.html'
    context_object_name = 'albums'


class AlbumDetail(DetailView):
    model = Album
    template_name = 'mp3/album_detail.html'

    def get_context_data(self, **kwargs):
        context = super(AlbumDetail, self).get_context_data(**kwargs)
        context['songs'] = self.get_object().song_set.all().order_by('-song_title')
        context['key'] = paystack.PAYSTACK_PUBLIC_KEY
        context['current_user'] = self.request.user
        # context['songs_count'] = context['songs'].count()
        instance = Album.objects.get(album_name=self.get_object())
        if self.request.user in instance.owned_by.all():
            print(True)
        return context

    def post(self, *args, **kwargs):
        paid_user_str = self.request.POST.get('paid_user')
        paid_user = User.objects.get(username=paid_user_str)
        album_name = self.request.POST.get('album_name')
        paid_album = Album.objects.get(album_name=album_name)
        paid_album.owned_by.add(paid_user)
        paid_album.save()
        return JsonResponse({'message': 'Payment successful'}, status=201)

    def get_success_url(self):
        return reverse('mp3:album_detail', kwargs={'slug': self.get_object().slug})


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_name', 'genre', 'price', 'album_logo']

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        form.save()
        return super(AlbumCreate, self).form_valid(form)


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_name', 'genre', 'price', 'album_logo']


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
