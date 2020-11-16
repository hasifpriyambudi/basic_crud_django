from django.shortcuts import render,redirect, HttpResponse
from perpustakaan.models import Buku
from .forms import FormBuku
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from .resource import BukuResource

def export_xls(request):
    buku = BukuResource()
    dataset = buku.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=buku.xls'
    return response

@login_required(login_url=settings.LOGIN_URL)
def signUp(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'User Berhasil dibuat!')
            return redirect('/sign-up')
        else:
            messages.error(request,'Terjadi Kesalahan!')
            return redirect('/sign-up')
    else:
        form = UserCreationForm()
        konteks = {
            'form':form
        }
        return render(request,'signup.html',konteks)


@login_required(login_url=settings.LOGIN_URL)
def ubahBuku(request,id_buku):
    buku = Buku.objects.get(id=id_buku)
    if request.POST:
        form = FormBuku(request.POST,request.FILES, instance=buku)
        if form.is_valid():
            form.save()
            messages.success(request,'Data Berhasil Diperbarui')
            return redirect('ubah-buku',id_buku=id_buku)
    else:
        form = FormBuku(instance=buku)
        konteks = {
            'form': form,
            'buku': buku,
        }
    return render(request,'ubah-buku.html',konteks)

@login_required(login_url=settings.LOGIN_URL)
def buku(request):
    books = Buku.objects.all() # Menampilkan Semua Row
    # books = Buku.objects.filter(kelompok__nama='Umum',jumlah=50)[:1] # Menampilkan Berdasarkan Filter Limit [:1]
    konteks = {
        'books': books,
    }
    return render(request,'buku.html',konteks)

@login_required(login_url=settings.LOGIN_URL)
def penerbit(request):
    return render(request,'penerbit.html')

@login_required(login_url=settings.LOGIN_URL)
def home(request):
    return render(request,'home.html')

@login_required(login_url=settings.LOGIN_URL)
def tambahBuku(request):
    if request.POST:
        form = FormBuku(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FormBuku()
            messages.success(request,'Data Berhasil Ditambah')
            konteks = {'form':form}
            # return redirect('/tambah-buku')
            return redirect('/tambah-buku',konteks)
    else:
        form = FormBuku()

        konteks = {'form':form}

    return render(request,'tambah-buku.html',konteks)

@login_required(login_url=settings.LOGIN_URL)
def hapusBuku(request,id_buku):
    buku = Buku.objects.filter(id=id_buku)
    buku.delete()

    messages.success(request,'Data Berhasil Dihapus')

    return redirect('/buku')