from django.contrib import admin
from burial_memories.models import BurialMemory, MemoryGallery, MemoryTribute, FamilyTree, Donation


class BurialMemoryAdmin(admin.ModelAdmin):
    list_display = ('by', 'title', 'first_name', 'last_name', 'created')
    list_filter = ('by', 'created', 'date_of_death', "cause_of_death")
    search_field = ('first_name', 'last_name')
    prepopulated_fields = {'slug': ('title', 'first_name', 'last_name',)}


admin.site.register(BurialMemory, BurialMemoryAdmin)

admin.site.register(MemoryGallery)

admin.site.register(FamilyTree)

admin.site.register(MemoryTribute)

admin.site.register(Donation)
