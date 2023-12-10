from django.db import models
from django.contrib.gis.db import models
from django.contrib.auth.models import User
import uuid
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

@deconstructible
class PDFValidator:
    def __call__(self, value):
        if not value.name.endswith('.pdf'):
            raise ValidationError('Only PDF files are allowed.')

class Informasi(models.Model):
    logo_plut = models.ImageField((""), upload_to='assets', height_field=None, width_field=None, max_length=None)
    logo_sidaku = models.ImageField((""), upload_to='assets', height_field=None, width_field=None, max_length=None)
    ket_plut = models.CharField(max_length=100)
    ket_sidaku = models.CharField(max_length=100)
    alamat_plut = models.CharField(max_length=100)
    telepon = models.CharField(max_length=13)
    email = models.EmailField()
    link_ig = models.CharField(max_length=100)
    link_fb = models.CharField(max_length=100)

class KontakLayanan(models.Model):
    fp_nahub = models.ImageField((""), upload_to='assets', height_field=None, width_field=None, max_length=None)
    nahub = models.CharField(max_length=50)
    wa_nahub = models.CharField(max_length=20)

class Pengaduan(models.Model):
    nama = models.CharField(max_length=50)
    telepon = models.CharField(max_length=13)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    pesan = models.TextField(max_length=500)

class Detail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    nik = models.CharField(max_length=16, unique=True, primary_key=True)
    telepon = models.CharField(max_length=13)
    foto_profil = models.ImageField((""), upload_to='assets', height_field=None, width_field=None, max_length=None)
    role = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.nik
    
class ProdukHukum(models.Model):
    nama = models.CharField(max_length=100, null=True)
    KATEGORI = (
        ("Undang-Undang", "Undang-Undang"),
        ("Perancangan Undang-Undang", "Perancangan Undang-Undang"),
        ("Peraturan Pemerintah", "Peraturan Pemerintah"),
        ("Peraturan Presiden", "Peraturan Presiden"),
        ("Keputusan dan Intruksi Presiden", "Keputusan dan Intruksi Presiden"),
        ("Peraturan Menteri", "Peraturan Menteri"),
        ("Keputusan Menteri", "Keputusan Menteri"),
        ("Keputusan Deputi", "Keputusan Deputi"),
        ("Peraturan Terkait", "Peraturan Terkait"),
        ("Petunjuk Pelaksanaan", "Petunjuk Pelaksanaan"),
        ("Surat Edaran", "Surat Edaran")
    )
    kategori = models.CharField(max_length=35, choices=KATEGORI)
    tahun = models.IntegerField(null=True)
    dokumen = models.FileField((""), upload_to='documents', null=True, validators=[PDFValidator()])
    
class RapatKoordinasi(models.Model):
    nama = models.CharField(max_length=100)
    KATEGORI = (
        ("Undang-Undang", "Undang-Undang"),
        ("Perancangan Undang-Undang", "Perancangan Undang-Undang"),
        ("Peraturan Pemerintah", "Peraturan Pemerintah"),
        ("Peraturan Presiden", "Peraturan Presiden"),
        ("Keputusan dan Intruksi Presiden", "Keputusan dan Intruksi Presiden"),
        ("Peraturan Menteri", "Peraturan Menteri"),
        ("Keputusan Menteri", "Keputusan Menteri"),
        ("Keputusan Deputi", "Keputusan Deputi"),
        ("Peraturan Terkait", "Peraturan Terkait"),
        ("Petunjuk Pelaksanaan", "Petunjuk Pelaksanaan"),
        ("Surat Edaran", "Surat Edaran")
    )
    kategori = models.CharField(max_length=35, choices=KATEGORI)
    dokumen = models.FileField((""), upload_to='documents', null=True, validators=[PDFValidator()])
    
class Paparan(models.Model):
    nama = models.CharField(max_length=100)
    dokumen = models.FileField((""), upload_to='documents', null=True, validators=[PDFValidator()])
    
class Berita(models.Model):
    judul = models.CharField(max_length=255)
    isi = models.TextField(max_length=5000)
    gambar = models.ImageField((""), upload_to='assets', height_field=None, width_field=None, max_length=None)
    views_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

class Fakta(models.Model):
    judul = models.CharField(max_length=50)
    isi = models.TextField(max_length=255)
    gambar = models.ImageField((""), upload_to='assets', height_field=None, width_field=None, max_length=None)
  
class Koperasi(models.Model):
    pemilik = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='owner_koperasi')
    username = models.CharField(max_length=20, unique=True, primary_key=True, default=uuid.uuid4)
    nama = models.CharField(max_length=50)
    alamat = models.CharField(max_length=255)
    foto_profil = models.ImageField((""), upload_to='assets', height_field=None, width_field=None, max_length=None)
    JENIS_KOPERASI = (
        ("Konsumen", "Konsumen"),
        ("Simpan Pinjam", "Simpan Pinjam"),
        ("Jasa", "Jasa"),
        ("Produsen", "Produsen"),
        ("Pemasaran", "Pemasaran")
    ) 
    jenis = models.CharField(max_length=13, choices=JENIS_KOPERASI)
    badan_hukum = models.CharField(max_length=50)
    ketua = models.CharField(max_length=50)
    sekretaris = models.CharField(max_length=50)
    bendahara = models.CharField(max_length=50)
    pengelola = models.CharField(max_length=50)
    pengawas = models.CharField(max_length=50)
    jml_anggota = models.IntegerField(null=True)
    jml_karyawan = models.IntegerField(null=True)
    tgl_rat = models.DateField()
    jml_hadir_rat = models.IntegerField(null=True)
    produk_unggulan = models.ImageField((""), upload_to='assets', height_field=None, width_field=None, max_length=None)
    simpanan = models.FileField((""), upload_to='documents', null=True, validators=[PDFValidator()])
    pinjaman = models.FileField((""), upload_to='documents', null=True, validators=[PDFValidator()])
    latitude = models.FloatField()
    longitude = models.FloatField()
    point = models.PointField(null=True)
    nama_pemilik = models.CharField(max_length=255)
    nib = models.CharField(max_length=13)
    nik = models.CharField(max_length=16)
    dok_ketua = models.FileField((""), upload_to='documents', null=True, validators=[PDFValidator()])
    dok_sekretaris = models.FileField((""), upload_to='documents', null=True, validators=[PDFValidator()])
    dok_bendahara = models.FileField((""), upload_to='documents', null=True, validators=[PDFValidator()])
    dok_pengelola = models.FileField((""), upload_to='documents', null=True, validators=[PDFValidator()])
    dok_pengawas = models.FileField((""), upload_to='documents', null=True, validators=[PDFValidator()])
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    label = models.CharField(max_length=10, null=True)
    
class JenisProdukKoperasi(models.Model):
    koperasi = models.ForeignKey(Koperasi, on_delete=models.CASCADE, null=True, related_name='jenis_produk_koperasi')
    foto_produk = models.ImageField((""), upload_to='assets', height_field=None, width_field=None, max_length=None)
    nama_produk = models.CharField(max_length=25, null=True)
    komoditi = models.CharField(null=True, max_length=50)
    volume = models.IntegerField(null=True)
    satuan = models.CharField(max_length=10, null=True)
    harga = models.IntegerField(null=True)
    total = models.IntegerField(null=True)
    
class UMKM(models.Model):
    pemilik = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='owner_umkm')
    username = models.CharField(max_length=25, unique=True, primary_key=True, default=uuid.uuid4)
    nama_pemilik = models.CharField(max_length=50)
    nomor_anggota = models.CharField(max_length=25)
    alamat_domisili = models.CharField(max_length=255)
    nik = models.CharField(max_length=16)
    telepon = models.CharField(max_length=13)
    email = models.EmailField(unique=True)
    foto_profil = models.ImageField((""), upload_to='assets', height_field=None, width_field=None, max_length=None)
    nama = models.CharField(max_length=50)
    alamat_usaha = models.CharField(max_length=255)
    BENTUK = (
        ("Perorangan", "Perorangan"),
        ("CV", "CV"),
        ("UD", "UD"),
        ("Koperasi", "Koperasi"),
        ("Lainnya", "Lainnya")
    )
    bentuk = models.CharField(max_length=10, choices=BENTUK)
    tahun_berdiri = models.IntegerField(null=True)
    BIDANG = (
        ("Makanan dalam Kemasan", "Makanan dalam Kemasan"),
        ("Minuman dalam Kemasan", "Minuman dalam Kemasan"),
        ("Kerajinan", "Kerajinan"),
        ("Perdagangan", "Perdagangan"),
        ("Jasa", "Jasa"),
        ("Lainnya", "Lainnya")
    )
    bidang = models.CharField(max_length=25, choices=BIDANG)
    wilayah_pemasaran = models.CharField(max_length=255)
    omzet = models.IntegerField(null=True)
    total_aset = models.IntegerField(null=True)
    SKALA = (
        ("Mikro", "Mikro"),
        ("Kecil", "Kecil"),
        ("Menengah", "Menengah")
    )
    skala = models.CharField(max_length=8, choices=SKALA)
    uraian_masalah = models.CharField(max_length=255)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    point = models.PointField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    label = models.CharField(max_length=10, null=True)
    
class JenisProdukUMKM(models.Model):
    umkm = models.ForeignKey(UMKM, on_delete=models.CASCADE, null=True, related_name='jenis_produk_umkm')
    foto_produk = models.ImageField((""), upload_to='assets', height_field=None, width_field=None, max_length=None)
    nama_produk = models.CharField(max_length=25, null=True)
    komoditi = models.CharField(max_length=20, null=True)
    volume = models.IntegerField(null=True)
    satuan = models.CharField(max_length=10, null=True)
    harga = models.IntegerField(null=True)
    total = models.IntegerField(null=True)
    
class PermintaanProduk(models.Model):
    umkm = models.ForeignKey(UMKM, on_delete=models.CASCADE, null=True, related_name='permintaan_produk_umkm')
    BULAN = (
        ("Januari", "Januari"),
        ("Februari", "Februari"),
        ("Maret", "Maret"),
        ("April", "April"),
        ("Mei", "Mei"),
        ("Juni", "Juni"),
        ("Juli", "Juli"),
        ("Agustus", "Agustus"),
        ("September", "September"),
        ("Oktober", "Oktober"),
        ("November", "November"),
        ("Desember", "Desember")
    )
    bulan = models.CharField(max_length=10, choices=BULAN)
    tahun = models.IntegerField(null=True)
    nama_produk = models.CharField(max_length=255)
    permintaan = models.IntegerField(null=True)
    produksi = models.IntegerField(null=True)
    
class PermintaanPemasok(models.Model):
    umkm = models.ForeignKey(UMKM, on_delete=models.CASCADE, null=True, related_name='permintaan_pemasok_umkm')
    BULAN = (
        ("Januari", "Januari"),
        ("Februari", "Februari"),
        ("Maret", "Maret"),
        ("April", "April"),
        ("Mei", "Mei"),
        ("Juni", "Juni"),
        ("Juli", "Juli"),
        ("Agustus", "Agustus"),
        ("September", "September"),
        ("Oktober", "Oktober"),
        ("November", "November"),
        ("Desember", "Desember")
    )
    bulan = models.CharField(max_length=10, choices=BULAN)
    tahun = models.IntegerField(null=True)
    PEMASOK = (
        ("Retailer", "Retailer"),
        ("Supplier", "Supplier")
    )
    pemasok = models.CharField(max_length=8)
    permintaan = models.IntegerField(null=True)
    produksi = models.IntegerField(null=True)
    
class PenilaianPemasok(models.Model):
    umkm = models.ForeignKey(UMKM, on_delete=models.CASCADE, null=True, related_name='penilaian_pemasok_umkm')
    nama = models.CharField(max_length=50)
    kualitas = models.IntegerField(null=True)
    pengiriman = models.IntegerField(null=True)
    biaya = models.IntegerField(null=True)
    
class PrioritasPemasok(models.Model):
    umkm = models.OneToOneField(UMKM, on_delete=models.CASCADE, null=True, related_name='prioritas_pemasok_umkm')
    kualitas_biaya = models.CharField(max_length=1, null=True)
    kualitas_pengiriman = models.CharField(max_length=1, null=True)
    biaya_pengiriman = models.CharField(max_length=1, null=True)
    
class TenagaKerja(models.Model):
    umkm = models.ForeignKey(UMKM, on_delete=models.CASCADE, null=True, related_name='tenaga_kerja_umkm')
    JENIS_KELAMIN = (
        ("Laki-laki", "Laki-laki"),
        ("Perempuan", "Perempuan")
    )
    jenis = models.CharField(max_length=10, choices=JENIS_KELAMIN)
    jumlah = models.IntegerField(null=True)
    PENDIDIKAN = (
        ("SD Sederajat", "SD Sederajat"),
        ("SMP Sederajat", "SMP Sederajat"),
        ("SMA Sederajat", "SMA Sederajat"),
        ("S1/S2/S3", "S1/S2/S3")
    )
    pendidikan = models.CharField(max_length=15, choices=PENDIDIKAN)
    
class Perijinan(models.Model):
    umkm = models.ForeignKey(UMKM, on_delete=models.CASCADE, null=True, related_name='perijinan_umkm')
    JENIS_PERIJINAN = (
        ("NIB", "NIB"),
        ("P-IRT", "P-IRT"),
        ("NPWP", "NPWP"),
        ("MERK", "MERK"),
        ("HALAL", "HALAL"),
        ("BPOM", "BPOM"),
        ("Akta Pendirian", "Akta Pendirian"),
        ("Lainnya", "Lainnya")
    )
    jenis = models.CharField(max_length=20, choices=JENIS_PERIJINAN)
    nomor = models.CharField(max_length=20, null=True)
    tanggal = models.DateField()
    
class BahanBaku(models.Model):
    umkm = models.ForeignKey(UMKM, on_delete=models.CASCADE, null=True, related_name='bahan_baku_umkm')
    jenis = models.CharField(max_length=50)
    volume = models.IntegerField(null=True)
    nilai = models.IntegerField(null=True)
    asal = models.CharField(max_length=50)
    
class PemakaianEnergi(models.Model):
    umkm = models.ForeignKey(UMKM, on_delete=models.CASCADE, null=True, related_name='pemakaian_energi_umkm')
    JENIS_ENERGI = (
        ("PLN", "PLN"),
        ("Bahan Bakar Generator/Genset", "Bahan Bakar Generator/Genset"),
        ("Bahan Bakar Gas LPG (3kg/12kg)", "Bahan Bakar Gas LPG (3kg/12kg)"),
        ("Air (PDAM/HIPAM/Sumur)", "Air (PDAM/HIPAM/Sumur)")
    )
    jenis = models.CharField(max_length=50, choices=JENIS_ENERGI)
    kapasitas = models.IntegerField(null=True)
    keterangan = models.CharField(max_length=50)
    
class AlatProduksi(models.Model):
    umkm = models.ForeignKey(UMKM, on_delete=models.CASCADE, null=True, related_name='alat_produksi_umkm')
    nama = models.CharField(max_length=50)
    
class Fasilitas(models.Model):
    umkm = models.ForeignKey(UMKM, on_delete=models.CASCADE, null=True, related_name='fasilitas_umkm')
    JENIS_FASILITAS = (
        ("ISO", "ISO"),
        ("SNI", "SNI"),
        ("SERTIFIKAT HALAL", "SERTIFIKAT HALAL"),
        ("MEREK DAGANG", "MEREK DAGANG"),
        ("UJI PRODUK", "UJI PRODUK"),
        ("ALAT/MESIN", "ALAT/MESIN"),
        ("Lainnya", "Lainnya")
    )
    jenis = models.CharField(max_length=20, choices=JENIS_FASILITAS)
    nama = models.CharField(max_length=50)
    tahun = models.IntegerField(null=True)
    
class Pelatihan(models.Model):
    umkm = models.ForeignKey(UMKM, on_delete=models.CASCADE, null=True, related_name='pelatihan_umkm')
    nama = models.CharField(max_length=50)
    tahun = models.IntegerField(null=True)
    tempat = models.CharField(max_length=50)
    
class LaporanKeuangan(models.Model):
    pemilik = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='owner_kumkm')
    koperasi = models.OneToOneField(Koperasi, on_delete=models.CASCADE, null=True, related_name='lapkeu_koperasi')
    umkm = models.OneToOneField(UMKM, on_delete=models.CASCADE, null=True, related_name='lapkeu_umkm')
    nama_KUMKM = models.CharField(max_length=50)
    BULAN = (
        ("Januari", "Januari"),
        ("Februari", "Februari"),
        ("Maret", "Maret"),
        ("April", "April"),
        ("Mei", "Mei"),
        ("Juni", "Juni"),
        ("Juli", "Juli"),
        ("Agustus", "Agustus"),
        ("September", "September"),
        ("Oktober", "Oktober"),
        ("November", "November"),
        ("Desember", "Desember")
    )
    bulan = models.CharField(max_length=10, choices=BULAN)
    tahun = models.IntegerField()
    laba_rugi = models.FileField((""), upload_to='documents', null=True, validators=[PDFValidator()])
    neraca = models.FileField((""), upload_to='documents', null=True, validators=[PDFValidator()])
    arus_kas = models.FileField((""), upload_to='documents', null=True, validators=[PDFValidator()])
    perubahan_modal = models.FileField((""), upload_to='documents', null=True, validators=[PDFValidator()])
    catatan_keuangan = models.FileField((""), upload_to='documents', null=True, validators=[PDFValidator()])
    kas = models.IntegerField()
    bank = models.IntegerField()
    pinjaman_anggota = models.IntegerField()
    pinjaman_macet = models.IntegerField()
    pendapatan_diterima = models.IntegerField()
    beban = models.IntegerField()
    piutang_tak_tertagih = models.IntegerField()
    aset_lancar = models.IntegerField()
    persediaan_barang = models.IntegerField()
    persediaan_konsinyasi = models.IntegerField()
    piutang_usaha = models.IntegerField()
    tanah = models.IntegerField()
    bangunan = models.IntegerField()
    peny_bangunan = models.IntegerField()
    inventaris_kantor = models.IntegerField()
    peny_invent_kantor = models.IntegerField()
    aset_tidak_lancar = models.IntegerField()
    simpanan_sukarela = models.IntegerField(null=True)
    simpanan_berjangka = models.IntegerField(null=True)
    hutang_usaha = models.IntegerField(null=True)
    beban_ymh_dibayar = models.IntegerField(null=True)
    hutang_lain_lain = models.IntegerField(null=True)
    simpanan_pokok = models.IntegerField()
    simpanan_wajib = models.IntegerField()
    donasi = models.IntegerField()
    cad = models.IntegerField()
    modal_penyertaan = models.IntegerField()
    pendapatan_jasa = models.IntegerField()
    pendapatan_administrasi = models.IntegerField()
    pendapatan_toko = models.IntegerField()
    pendapatan_lainnya = models.IntegerField()
    hpp = models.IntegerField()
    jasa_simpanan = models.IntegerField()
    jasa_bank = models.IntegerField()
    jasa_simpanan_lain = models.IntegerField()
    jasa_simpanan_berjangka = models.IntegerField()
    jasa_simpanan_khusus = models.IntegerField()
    biaya_asuransi = models.IntegerField()
    biaya_penysh_piutang_tak_tertagih = models.IntegerField(null=True)
    biaya_audit = models.IntegerField()
    biaya_pajak = models.IntegerField()
    biaya_keuangan_lain = models.IntegerField()
    biaya_rapat_pengurus = models.IntegerField()
    biaya_rapat_anggota = models.IntegerField()
    biaya_perjalanan_dinas = models.IntegerField()
    biaya_diklat = models.IntegerField()
    honor_pengurus = models.IntegerField()
    biaya_pembinaan = models.IntegerField()
    biaya_org_lain = models.IntegerField()
    gaji_karyawan = models.IntegerField()
    tunjangan = models.IntegerField()
    konsumsi = models.IntegerField()
    biaya_transport_dinas = models.IntegerField()
    biaya_pendidikan = models.IntegerField()
    biaya_karyawan_lain = models.IntegerField()
    biaya_alat_tulis = models.IntegerField()
    biaya_listrik = models.IntegerField()
    biaya_telepon = models.IntegerField()
    biaya_air = models.IntegerField()
    biaya_ops_lain = models.IntegerField()