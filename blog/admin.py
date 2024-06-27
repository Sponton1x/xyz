from django.contrib import admin
from .models import Project, About, Blog, Technology, Certificates, Document


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on', 'show_link')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ['title', 'content']


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on', 'show_link')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Certificates)
class CertificatesAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('name',)
