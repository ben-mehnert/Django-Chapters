# admin.py
from django import forms
from mptt.admin import MPTTModelAdmin
from .models import Chapter, File
from django.contrib import admin
from django.utils.html import format_html

class ChapterAdminForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = '__all__'
        widgets = {
            'context': forms.Textarea(attrs={'rows': 10, 'cols': 80, 'class': 'markdown-editor'}),
        }

class FileInline(admin.TabularInline):  # Use TabularInline for a table-like representation
    model = File

class ChapterAdmin(MPTTModelAdmin):
    form = ChapterAdminForm
    list_display = ('name', 'parent', 'get_level', 'context_display')
    search_fields = ('name', 'context')
    inlines = [FileInline]  # Add the FileInline to the inlines list

    class Media:
        css = {
            'all': ('css/admin.css',),
        }

    fieldsets = (
        (None, {
            'fields': ('name', 'parent', 'context'),
        }),
    )

    def context_display(self, obj):
        return format_html(obj.context) if obj.context else ""
    context_display.short_description = 'Context'

admin.site.register(Chapter, ChapterAdmin)
