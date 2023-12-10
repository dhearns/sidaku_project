# Generated by Django 4.2.2 on 2023-07-17 15:17

import base.models
from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Berita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=255)),
                ('isi', models.TextField(max_length=5000)),
                ('gambar', models.ImageField(upload_to='assets', verbose_name='')),
                ('views_count', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Informasi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo_plut', models.ImageField(upload_to='assets', verbose_name='')),
                ('logo_sidaku', models.ImageField(upload_to='assets', verbose_name='')),
                ('ket_plut', models.CharField(max_length=100)),
                ('ket_sidaku', models.CharField(max_length=100)),
                ('alamat_plut', models.CharField(max_length=100)),
                ('telepon', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=254)),
                ('link_ig', models.CharField(max_length=100)),
                ('link_fb', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='KontakPelayanan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fp_nahub1', models.ImageField(upload_to='assets', verbose_name='')),
                ('fp_nahub2', models.ImageField(upload_to='assets', verbose_name='')),
                ('nahub1', models.CharField(max_length=50)),
                ('nahub2', models.CharField(max_length=50)),
                ('wa_nahub1', models.CharField(max_length=20)),
                ('wa_nahub2', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Koperasi',
            fields=[
                ('username', models.CharField(default=uuid.uuid4, max_length=20, primary_key=True, serialize=False, unique=True)),
                ('nama', models.CharField(max_length=50)),
                ('alamat', models.CharField(max_length=255)),
                ('foto_profil', models.ImageField(upload_to='assets', verbose_name='')),
                ('jenis', models.CharField(choices=[('Konsumen', 'Konsumen'), ('Simpan Pinjam', 'Simpan Pinjam'), ('Jasa', 'Jasa'), ('Produsen', 'Produsen'), ('Pemasaran', 'Pemasaran')], max_length=13)),
                ('badan_hukum', models.CharField(max_length=50)),
                ('ketua', models.CharField(max_length=50)),
                ('sekretaris', models.CharField(max_length=50)),
                ('bendahara', models.CharField(max_length=50)),
                ('pengelola', models.CharField(max_length=50)),
                ('pengawas', models.CharField(max_length=50)),
                ('jml_anggota', models.IntegerField(null=True)),
                ('jml_karyawan', models.IntegerField(null=True)),
                ('tgl_rat', models.DateField()),
                ('jml_hadir_rat', models.IntegerField(null=True)),
                ('produk_unggulan', models.ImageField(upload_to='assets', verbose_name='')),
                ('simpanan', models.FileField(null=True, upload_to='documents', validators=[base.models.PDFValidator()], verbose_name='')),
                ('pinjaman', models.FileField(null=True, upload_to='documents', validators=[base.models.PDFValidator()], verbose_name='')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('point', django.contrib.gis.db.models.fields.PointField(null=True, srid=4326)),
                ('tgl_penginputan', models.DateField()),
                ('nama_pemilik', models.CharField(max_length=255)),
                ('nib', models.CharField(max_length=13)),
                ('nik', models.CharField(max_length=16)),
                ('dok_ketua', models.FileField(null=True, upload_to='documents', validators=[base.models.PDFValidator()], verbose_name='')),
                ('dok_sekretaris', models.FileField(null=True, upload_to='documents', validators=[base.models.PDFValidator()], verbose_name='')),
                ('dok_bendahara', models.FileField(null=True, upload_to='documents', validators=[base.models.PDFValidator()], verbose_name='')),
                ('dok_pengelola', models.FileField(null=True, upload_to='documents', validators=[base.models.PDFValidator()], verbose_name='')),
                ('dok_pengawas', models.FileField(null=True, upload_to='documents', validators=[base.models.PDFValidator()], verbose_name='')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('label', models.CharField(max_length=10, null=True)),
                ('pemilik', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner_koperasi', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Paparan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('dokumen', models.FileField(null=True, upload_to='documents', validators=[base.models.PDFValidator()], verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='ProdukHukum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100, null=True)),
                ('kategori', models.CharField(choices=[('Undang-Undang', 'Undang-Undang'), ('Perancangan Undang-Undang', 'Perancangan Undang-Undang'), ('Peraturan Pemerintah', 'Peraturan Pemerintah'), ('Peraturan Presiden', 'Peraturan Presiden'), ('Keputusan dan Intruksi Presiden', 'Keputusan dan Intruksi Presiden'), ('Peraturan Menteri', 'Peraturan Menteri'), ('Keputusan Menteri', 'Keputusan Menteri'), ('Keputusan Deputi', 'Keputusan Deputi'), ('Peraturan Terkait', 'Peraturan Terkait'), ('Petunjuk Pelaksanaan', 'Petunjuk Pelaksanaan'), ('Surat Edaran', 'Surat Edaran')], max_length=35)),
                ('tahun', models.IntegerField(null=True)),
                ('dokumen', models.FileField(null=True, upload_to='documents', validators=[base.models.PDFValidator()], verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='RapatKoordinasi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('kategori', models.CharField(choices=[('Undang-Undang', 'Undang-Undang'), ('Perancangan Undang-Undang', 'Perancangan Undang-Undang'), ('Peraturan Pemerintah', 'Peraturan Pemerintah'), ('Peraturan Presiden', 'Peraturan Presiden'), ('Keputusan dan Intruksi Presiden', 'Keputusan dan Intruksi Presiden'), ('Peraturan Menteri', 'Peraturan Menteri'), ('Keputusan Menteri', 'Keputusan Menteri'), ('Keputusan Deputi', 'Keputusan Deputi'), ('Peraturan Terkait', 'Peraturan Terkait'), ('Petunjuk Pelaksanaan', 'Petunjuk Pelaksanaan'), ('Surat Edaran', 'Surat Edaran')], max_length=35)),
                ('dokumen', models.FileField(null=True, upload_to='documents', validators=[base.models.PDFValidator()], verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='UMKM',
            fields=[
                ('username', models.CharField(default=uuid.uuid4, max_length=20, primary_key=True, serialize=False, unique=True)),
                ('nama_pemilik', models.CharField(max_length=50)),
                ('nomor_anggota', models.CharField(max_length=25)),
                ('alamat_domisili', models.CharField(max_length=255)),
                ('nik', models.CharField(max_length=16)),
                ('telepon', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('foto_profil', models.ImageField(upload_to='assets', verbose_name='')),
                ('nama_usaha', models.CharField(max_length=50)),
                ('alamat_usaha', models.CharField(max_length=255)),
                ('bentuk', models.CharField(choices=[('Perorangan', 'Perorangan'), ('CV', 'CV'), ('UD', 'UD'), ('Koperasi', 'Koperasi'), ('Lainnya', 'Lainnya')], max_length=10)),
                ('tahun_berdiri', models.IntegerField(null=True)),
                ('bidang', models.CharField(choices=[('Makanan dalam Kemasan', 'Makanan dalam Kemasan'), ('Minuman dalam Kemasan', 'Minuman dalam Kemasan'), ('Kerajinan', 'Kerajinan'), ('Perdagangan', 'Perdagangan'), ('Jasa', 'Jasa'), ('Lainnya', 'Lainnya')], max_length=25)),
                ('wilayah_pemasaran', models.CharField(max_length=255)),
                ('omzet', models.IntegerField(null=True)),
                ('total_aset', models.IntegerField(null=True)),
                ('skala', models.CharField(choices=[('Mikro', 'Mikro'), ('Kecil', 'Kecil'), ('Menengah', 'Menengah')], max_length=8)),
                ('uraian_masalah', models.CharField(max_length=255)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('point', django.contrib.gis.db.models.fields.PointField(null=True, srid=4326)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('label', models.CharField(max_length=10, null=True)),
                ('pemilik', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner_umkm', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TenagaKerja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jenis', models.CharField(choices=[('Laki-laki', 'Laki-laki'), ('Perempuan', 'Perempuan')], max_length=10)),
                ('jumlah', models.IntegerField(null=True)),
                ('pendidikan', models.CharField(choices=[('SD Sederajat', 'SD Sederajat'), ('SMP Sederajat', 'SMP Sederajat'), ('SMA Sederajat', 'SMA Sederajat'), ('S1/S2/S3', 'S1/S2/S3')], max_length=15)),
                ('umkm', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tenaga_kerja_umkm', to='base.umkm')),
            ],
        ),
        migrations.CreateModel(
            name='PermintaanProduk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bulan', models.CharField(choices=[('Januari', 'Januari'), ('Februari', 'Februari'), ('Maret', 'Maret'), ('April', 'April'), ('Mei', 'Mei'), ('Juni', 'Juni'), ('Juli', 'Juli'), ('Agustus', 'Agustus'), ('September', 'September'), ('Oktober', 'Oktober'), ('November', 'November'), ('Desember', 'Desember')], max_length=10)),
                ('tahun', models.IntegerField(null=True)),
                ('nama_produk', models.CharField(max_length=255)),
                ('permintaan', models.IntegerField(null=True)),
                ('produksi', models.IntegerField(null=True)),
                ('umkm', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='permintaan_produk_umkm', to='base.umkm')),
            ],
        ),
        migrations.CreateModel(
            name='PermintaanPemasok',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bulan', models.CharField(choices=[('Januari', 'Januari'), ('Februari', 'Februari'), ('Maret', 'Maret'), ('April', 'April'), ('Mei', 'Mei'), ('Juni', 'Juni'), ('Juli', 'Juli'), ('Agustus', 'Agustus'), ('September', 'September'), ('Oktober', 'Oktober'), ('November', 'November'), ('Desember', 'Desember')], max_length=10)),
                ('tahun', models.IntegerField(null=True)),
                ('pemasok', models.CharField(max_length=8)),
                ('permintaan', models.IntegerField(null=True)),
                ('produksi', models.IntegerField(null=True)),
                ('umkm', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='permintaan_pemasok_umkm', to='base.umkm')),
            ],
        ),
        migrations.CreateModel(
            name='Perijinan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jenis', models.CharField(choices=[('NIB', 'NIB'), ('P-IRT', 'P-IRT'), ('NPWP', 'NPWP'), ('MERK', 'MERK'), ('HALAL', 'HALAL'), ('BPOM', 'BPOM'), ('Akta Pendirian', 'Akta Pendirian'), ('Lainnya', 'Lainnya')], max_length=20)),
                ('nomor', models.CharField(max_length=50)),
                ('tanggal', models.DateField()),
                ('umkm', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='perijinan_umkm', to='base.umkm')),
            ],
        ),
        migrations.CreateModel(
            name='PenilaianPemasok',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_pemasok', models.CharField(max_length=50)),
                ('kualitas', models.IntegerField(null=True)),
                ('pengiriman', models.IntegerField(null=True)),
                ('harga', models.IntegerField(null=True)),
                ('kualitas_harga', models.IntegerField(null=True)),
                ('kualitas_pengiriman', models.IntegerField(null=True)),
                ('harga_pengiriman', models.IntegerField(null=True)),
                ('umkm', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='penilaian_pemasok_umkm', to='base.umkm')),
            ],
        ),
        migrations.CreateModel(
            name='PemakaianEnergi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jenis', models.CharField(choices=[('PLN', 'PLN'), ('Bahan Bakar Generator/Genset', 'Bahan Bakar Generator/Genset'), ('Bahan Bakar Gas LPG (3kg/12kg)', 'Bahan Bakar Gas LPG (3kg/12kg)'), ('Air (PDAM/HIPAM/Sumur)', 'Air (PDAM/HIPAM/Sumur)')], max_length=50)),
                ('kapasitas', models.IntegerField(null=True)),
                ('keterangan', models.CharField(max_length=50)),
                ('umkm', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pemakaian_energi_umkm', to='base.umkm')),
            ],
        ),
        migrations.CreateModel(
            name='Pelatihan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('tahun', models.IntegerField(null=True)),
                ('tempat', models.CharField(max_length=50)),
                ('umkm', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pelatihan_umkm', to='base.umkm')),
            ],
        ),
        migrations.CreateModel(
            name='LaporanKeuangan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_KUMKM', models.CharField(max_length=50)),
                ('bulan', models.CharField(choices=[('Januari', 'Januari'), ('Februari', 'Februari'), ('Maret', 'Maret'), ('April', 'April'), ('Mei', 'Mei'), ('Juni', 'Juni'), ('Juli', 'Juli'), ('Agustus', 'Agustus'), ('September', 'September'), ('Oktober', 'Oktober'), ('November', 'November'), ('Desember', 'Desember')], max_length=10)),
                ('tahun', models.IntegerField()),
                ('laba_rugi', models.FileField(null=True, upload_to='documents', validators=[base.models.PDFValidator()], verbose_name='')),
                ('neraca', models.FileField(null=True, upload_to='documents', validators=[base.models.PDFValidator()], verbose_name='')),
                ('arus_kas', models.FileField(null=True, upload_to='documents', validators=[base.models.PDFValidator()], verbose_name='')),
                ('perubahan_modal', models.FileField(null=True, upload_to='documents', validators=[base.models.PDFValidator()], verbose_name='')),
                ('catatan_keuangan', models.FileField(null=True, upload_to='documents', validators=[base.models.PDFValidator()], verbose_name='')),
                ('kas', models.IntegerField()),
                ('bank', models.IntegerField()),
                ('pinjaman_anggota', models.IntegerField()),
                ('pinjaman_macet', models.IntegerField()),
                ('pendapatan_diterima', models.IntegerField()),
                ('beban', models.IntegerField()),
                ('piutang_tak_tertagih', models.IntegerField()),
                ('aset_lancar', models.IntegerField()),
                ('persediaan_barang', models.IntegerField()),
                ('persediaan_konsinyasi', models.IntegerField()),
                ('piutang_usaha', models.IntegerField()),
                ('tanah', models.IntegerField()),
                ('bangunan', models.IntegerField()),
                ('peny_bangunan', models.IntegerField()),
                ('inventaris_kantor', models.IntegerField()),
                ('peny_invent_kantor', models.IntegerField()),
                ('aset_tidak_lancar', models.IntegerField()),
                ('simpanan_sukarela', models.IntegerField(null=True)),
                ('simpanan_berjangka', models.IntegerField(null=True)),
                ('hutang_usaha', models.IntegerField(null=True)),
                ('beban_ymh_dibayar', models.IntegerField(null=True)),
                ('hutang_lain_lain', models.IntegerField(null=True)),
                ('simpanan_pokok', models.IntegerField()),
                ('simpanan_wajib', models.IntegerField()),
                ('donasi', models.IntegerField()),
                ('cad', models.IntegerField()),
                ('modal_penyertaan', models.IntegerField()),
                ('pendapatan_jasa', models.IntegerField()),
                ('pendapatan_administrasi', models.IntegerField()),
                ('pendapatan_toko', models.IntegerField()),
                ('pendapatan_lainnya', models.IntegerField()),
                ('hpp', models.IntegerField()),
                ('jasa_simpanan', models.IntegerField()),
                ('jasa_bank', models.IntegerField()),
                ('jasa_simpanan_lain', models.IntegerField()),
                ('jasa_simpanan_berjangka', models.IntegerField()),
                ('jasa_simpanan_khusus', models.IntegerField()),
                ('biaya_asuransi', models.IntegerField()),
                ('biaya_penysh_piutang_tak_tertagih', models.IntegerField(null=True)),
                ('biaya_audit', models.IntegerField()),
                ('biaya_pajak', models.IntegerField()),
                ('biaya_keuangan_lain', models.IntegerField()),
                ('biaya_rapat_pengurus', models.IntegerField()),
                ('biaya_rapat_anggota', models.IntegerField()),
                ('biaya_perjalanan_dinas', models.IntegerField()),
                ('biaya_diklat', models.IntegerField()),
                ('honor_pengurus', models.IntegerField()),
                ('biaya_pembinaan', models.IntegerField()),
                ('biaya_org_lain', models.IntegerField()),
                ('gaji_karyawan', models.IntegerField()),
                ('tunjangan', models.IntegerField()),
                ('konsumsi', models.IntegerField()),
                ('biaya_transport_dinas', models.IntegerField()),
                ('biaya_pendidikan', models.IntegerField()),
                ('biaya_karyawan_lain', models.IntegerField()),
                ('biaya_alat_tulis', models.IntegerField()),
                ('biaya_listrik', models.IntegerField()),
                ('biaya_telepon', models.IntegerField()),
                ('biaya_air', models.IntegerField()),
                ('biaya_ops_lain', models.IntegerField()),
                ('koperasi', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lapkeu_koperasi', to='base.koperasi')),
                ('pemilik', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner_kumkm', to=settings.AUTH_USER_MODEL)),
                ('umkm', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lapkeu_umkm', to='base.umkm')),
            ],
        ),
        migrations.CreateModel(
            name='JenisProdukUMKM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto_produk', models.ImageField(upload_to='assets', verbose_name='')),
                ('komoditi', models.IntegerField(null=True)),
                ('volume', models.IntegerField(null=True)),
                ('satuan', models.CharField(max_length=10, null=True)),
                ('harga', models.IntegerField(null=True)),
                ('total', models.IntegerField(null=True)),
                ('umkm', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jenis_produk_umkm', to='base.umkm')),
            ],
        ),
        migrations.CreateModel(
            name='JenisProdukKoperasi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto_produk', models.ImageField(upload_to='assets', verbose_name='')),
                ('komoditi', models.CharField(max_length=50, null=True)),
                ('volume', models.IntegerField(null=True)),
                ('satuan', models.CharField(max_length=10, null=True)),
                ('harga', models.IntegerField(null=True)),
                ('total', models.IntegerField(null=True)),
                ('koperasi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jenis_produk_koperasi', to='base.koperasi')),
            ],
        ),
        migrations.CreateModel(
            name='Fasilitas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jenis', models.CharField(choices=[('ISO', 'ISO'), ('SNI', 'SNI'), ('SERTIFIKAT HALAL', 'SERTIFIKAT HALAL'), ('MEREK DAGANG', 'MEREK DAGANG'), ('UJI PRODUK', 'UJI PRODUK'), ('ALAT/MESIN', 'ALAT/MESIN'), ('Lainnya', 'Lainnya')], max_length=20)),
                ('nama', models.CharField(max_length=50)),
                ('tahun', models.IntegerField(null=True)),
                ('umkm', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fasilitas_umkm', to='base.umkm')),
            ],
        ),
        migrations.CreateModel(
            name='Fakta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=50)),
                ('isi', models.TextField(max_length=255)),
                ('gambar', models.ImageField(upload_to='assets', verbose_name='')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('nik', models.CharField(max_length=16, primary_key=True, serialize=False, unique=True)),
                ('telepon', models.CharField(max_length=13)),
                ('foto_profil', models.ImageField(upload_to='assets', verbose_name='')),
                ('role', models.CharField(max_length=10, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BahanBaku',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jenis', models.CharField(max_length=50)),
                ('volume', models.IntegerField(null=True)),
                ('nilai', models.IntegerField(null=True)),
                ('asal', models.CharField(max_length=50)),
                ('umkm', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bahan_baku_umkm', to='base.umkm')),
            ],
        ),
        migrations.CreateModel(
            name='AlatProduksi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('umkm', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='alat_produksi_umkm', to='base.umkm')),
            ],
        ),
    ]
