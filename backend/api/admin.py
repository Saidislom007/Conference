from django.contrib import admin

from .models import Conference, WordPart


@admin.register(Conference)
class ConferenceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'type', 'slug')
    search_fields = ('title', 'type')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(WordPart)
class WordPartAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'conference',
        'maqola_soni',
        'bet_soni',
        'yaratilgan_sana',
    )
    search_fields = ('conference__title',)
    list_filter = ('yaratilgan_sana', 'conference')