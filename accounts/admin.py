from django.contrib import admin
from .models import Profile


# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'updated')
    list_display_links = ('user',)
    list_filter = ('user', 'phone')
    readonly_fields = ('slug', 'image_tag')
    # prepopulated_fields = {'slug': ('phone',)}
    search_fields = ('user', 'phone')

    ordering = ('-time_stamp',)
    fieldsets = (
        ('Basic Information', {'description': "Copy User UUID From Firebase Using Corresponding User Phone Number",
                               'fields': ('image_tag', 'phone', 'image', ('user',))}),
        ('Complete Full Information', {'classes': ('collapse',), 'fields': ('bio', ('gender'))}),)


admin.site.site_header = 'NWABEN ADMIN'
