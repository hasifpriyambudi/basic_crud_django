from django.contrib import admin
from perpustakaan.models import Buku, Kelompok
# Register your models here.

class BukuAdmin(admin.ModelAdmin):
    list_display = ['judul','penulis','kelompok','jumlah']
    search_fields = ['judul','penulis','penerbit']
    list_filter = ['kelompok','penulis']
    list_per_page = 4

admin.site.register(Buku, BukuAdmin)
admin.site.register(Kelompok)