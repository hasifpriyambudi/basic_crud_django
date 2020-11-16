from import_export import resources
from perpustakaan.models import Buku
from import_export.fields import Field

class BukuResource(resources.ModelResource):
    kelompok__nama = Field(attribute='kelompok', column_name='Kelompok')
    class Meta:
        model = Buku
        fields = ['judul','tanggal','kelompok__nama','penerbit','jumlah']
        export_order = ['judul','kelompok__nama','jumlah','penerbit','tanggal']