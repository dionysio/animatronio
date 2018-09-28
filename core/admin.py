# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import TaggedPicture


class TaggedPictureAdmin(admin.ModelAdmin):
    model = TaggedPicture
    list_display = ['title', 'caption', 'created',  'is_public', 'photo', 'tag_names', ]
    list_filter = ['created', 'is_public', 'tags']
    search_fields = ['title', 'caption', 'tags']
    readonly_fields = ['created']


admin.site.register(TaggedPicture, TaggedPictureAdmin)
