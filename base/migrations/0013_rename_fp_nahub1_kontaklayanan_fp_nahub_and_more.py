# Generated by Django 4.2.2 on 2023-07-29 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_rename_nama_usaha_umkm_nama'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kontaklayanan',
            old_name='fp_nahub1',
            new_name='fp_nahub',
        ),
        migrations.RenameField(
            model_name='kontaklayanan',
            old_name='nahub1',
            new_name='nahub',
        ),
        migrations.RenameField(
            model_name='kontaklayanan',
            old_name='wa_nahub1',
            new_name='wa_nahub',
        ),
        migrations.RemoveField(
            model_name='kontaklayanan',
            name='fp_nahub2',
        ),
        migrations.RemoveField(
            model_name='kontaklayanan',
            name='nahub2',
        ),
        migrations.RemoveField(
            model_name='kontaklayanan',
            name='wa_nahub2',
        ),
    ]
