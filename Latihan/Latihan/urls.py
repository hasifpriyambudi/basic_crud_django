from django.contrib import admin
from django.urls import path
from perpustakaan.views import *
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('buku/', buku),
    path('penerbit/', penerbit),
    path('', home),
    path('tambah-buku',tambahBuku),
    path('buku/ubah/<int:id_buku>',ubahBuku,name='ubah-buku'), # Parameter URL using <int:ARG> for integer
    path('buku/hapus/<int:id_buku>',hapusBuku,name='hapus-buku'),
    path('masuk/', LoginView.as_view(), name='masuk'),
    path('keluar/',LogoutView.as_view(), name='keluar'),
    path('sign-up/',signUp, name='sign-up'),
    path('export/xls', export_xls, name='export_xls')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)