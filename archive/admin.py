import os
# from audiofield.admin import AudioFileAdmin
from django.contrib import admin
from .models import Album, Song


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('uploaded_by', 'artist', 'album_name')
    actions = ['custom_delete_selected']
    list_filter = ('uploaded_by', 'artist', 'date_uploaded', 'genre')
    search_field = ('album_name', 'artist')
    prepopulated_fields = {'slug': ('album_name',)}

# list_display = (..., 'audio_file_player', ...)
# actions = ['custom_delete_selected']
#
#
# def custom_delete_selected(self, request, queryset):
#     # custom delete code
#     n = queryset.count()
#     for i in queryset:
#         if i.audio_file:
#             if os.path.exists(i.audio_file.path):
#                 os.remove(i.audio_file.path)
#         i.delete()
#     self.message_user(request, "Successfully deleted %d audio files." % n)
#
#
# custom_delete_selected.short_description = "Delete selected items"
#
#
# def get_actions(self, request):
#     actions = super(AudioFileAdmin, self).get_actions(request)
#     del actions['delete_selected']
#     return actions


admin.site.register(Album, AlbumAdmin)


class SongAdmin(admin.ModelAdmin):
    list_display = ('album', 'song_title',)

admin.site.register(Song, SongAdmin)