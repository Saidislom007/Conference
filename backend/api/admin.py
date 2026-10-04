from django.contrib import admin

from .models import (
    Conference,
    Maqola,
    AboutShoba,
    Shoba,
    WordPart
)


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


@admin.register(Maqola)
class MaqolaAdmin(admin.ModelAdmin):

    list_display = ('id', 'title')
    search_fields = ('title',)


@admin.register(AboutShoba)
class AboutShobaAdmin(admin.ModelAdmin):

    list_display = ('id', 'title')
    search_fields = ('title',)


@admin.register(Shoba)
class ShobaAdmin(admin.ModelAdmin):

    list_display = ('id', 'title')
    search_fields = ('title',)