# Generated by Django 3.1.3 on 2020-11-14 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perpustakaan', '0004_auto_20201114_1255'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buku',
            old_name='kelompok_id',
            new_name='kelompok',
        ),
    ]
