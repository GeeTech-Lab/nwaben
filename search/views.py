from django.db.models import Q
from django.shortcuts import render
from django.views import View

from mp3.models import Song, Album


class SearchView(View):

    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('q')
        if query:
            album_qs = Album.objects.filter(uploaded_by=self.request.user).filter(
                Q(album_name__icontains=query) | Q(artist__icontains=query)
            ).distinct()
            song_qs = Song.objects.all().filter(
                Q(song_title__icontains=query) | Q(album__album_name__icontains=query)
            ).distinct()
            return render(request, 'includes/search_result.html', {'album_qs': album_qs, 'song_qs': song_qs})
        return render(request, 'search_error.html')