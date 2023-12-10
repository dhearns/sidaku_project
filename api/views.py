import json
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import MyTokenObtainPairSerializer
from base.models import ProdukHukum, RapatKoordinasi, Paparan, Berita, Fakta, LaporanKeuangan, Koperasi, UMKM, JenisProdukKoperasi, JenisProdukUMKM, PermintaanProduk, PermintaanPemasok, PenilaianPemasok, PrioritasPemasok, TenagaKerja, Perijinan, BahanBaku, PemakaianEnergi, AlatProduksi, Fasilitas, Pelatihan, Informasi, KontakLayanan
from .serializers import ProdukHukumSerializer, RapatKoordinasiSerializer, PaparanSerializer, BeritaSerializer, FaktaSerializer, ChangePasswordSerializer, RegisterSerializer, LaporanKeuanganSerializer, KoperasiSerializer, JenisProdukKoperasiSerializer, UMKMSerializer, JenisProdukUMKMSerializer, PermintaanProdukSerializer, PermintaanPemasokSerializer, PenilaianPemasokSerializer, PrioritasPemasokSerializer, TenagaKerjaSerializer, PerijinanSerializer, BahanBakuSerializer, PemakaianEnergiSerializer, AlatProduksiSerializer, FasilitasSerializer, PelatihanSerializer, GambarSerializer, InformasiSerializer, KontakLayananSerializer
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core.serializers import serialize
from django.views.generic.base import TemplateView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from base.permissions import IsUMKMOrReadOnly, IsKoperasiOrReadOnly, IsSuperAdminOrReadOnly
from collections import Counter
from django.db.models import Sum
from .serializers import PengaduanSerializer
from django.core.mail import send_mail
from rest_framework.renderers import JSONRenderer


class RegisterViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [IsSuperAdminOrReadOnly]
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['username'] 
    search_fields = ['username']
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        
        return Response({"message": "Data deleted successfully"})
    
class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data['refresh_token']

            token = RefreshToken(refresh_token)

            token.blacklist()

            return Response({'message': 'Berhasil Logout'}, status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response({'message':'Gagal Logout'}, status=status.HTTP_400_BAD_REQUEST)

class ChangePasswordViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({"message": "Password updated!"})

class ProdukHukumViewSet(ModelViewSet):
    queryset = ProdukHukum.objects.all()
    serializer_class = ProdukHukumSerializer
    permission_classes = [IsSuperAdminOrReadOnly]
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['nama', 'kategori', 'tahun'] 
    search_fields = ['nama', 'kategori', 'tahun']
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        
        return Response({"message": "Data deleted successfully"})

class RapatKoordinasiViewSet(ModelViewSet):
    queryset = RapatKoordinasi.objects.all()
    serializer_class = RapatKoordinasiSerializer
    permission_classes = [IsSuperAdminOrReadOnly]
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['nama', 'kategori']  
    search_fields = ['nama', 'kategori']
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        
        return Response({"message": "Data deleted successfully"})

class PaparanViewSet(ModelViewSet):
    queryset = Paparan.objects.all()
    serializer_class = PaparanSerializer
    permission_classes = [IsSuperAdminOrReadOnly]
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['nama']
    search_fields = ['nama']
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        
        return Response({"message": "Data deleted successfully"})
    
class BeritaViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer]
    queryset = Berita.objects.all()
    serializer_class = BeritaSerializer
    permission_classes = [IsSuperAdminOrReadOnly]
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['judul']
    search_fields = ['judul']
    
    def retrieve(self, request, pk):
        article = Berita.objects.get(id=pk)
        article.views_count += 1
        article.save()
        serializer = BeritaSerializer(article)

        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        
        return Response({"message": "Data deleted successfully"})

class GambarViewSet(generics.ListCreateAPIView):
    queryset = Berita.objects.all()
    serializer_class = GambarSerializer
    
class FaktaViewSet(ModelViewSet):
    queryset = Fakta.objects.all()
    serializer_class = FaktaSerializer
    permission_classes = [IsSuperAdminOrReadOnly]
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        
        return Response({"message": "Data deleted successfully"})

class MarkersMapView(TemplateView):
    template_name = "map.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        umkm_data = list(UMKM.objects.all())
        koperasi_data = list(Koperasi.objects.all())
        kumkm_data = umkm_data + koperasi_data
        kumkm = json.loads(serialize("geojson", kumkm_data))
        context["markers"] = kumkm
        return context
   
class KoperasiViewSet(ModelViewSet):
    queryset = Koperasi.objects.all()
    serializer_class = KoperasiSerializer
    permission_classes = [IsSuperAdminOrReadOnly | IsKoperasiOrReadOnly]
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['nama'] 
    search_fields = ['nama']
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        
        return Response({"message": "Data deleted successfully"})

class JenisProdukKoperasiViewSet(ModelViewSet):
    queryset = JenisProdukKoperasi.objects.all()
    serializer_class = JenisProdukKoperasiSerializer
    permission_classes = [IsSuperAdminOrReadOnly | IsKoperasiOrReadOnly]

class UMKMViewSet(ModelViewSet):
    queryset = UMKM.objects.all()
    serializer_class = UMKMSerializer
    permission_classes = [IsSuperAdminOrReadOnly | IsUMKMOrReadOnly]
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['nama']
    search_fields = ['nama']
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        
        return Response({"message": "Data deleted successfully"})

class JenisProdukUMKMViewSet(ModelViewSet):
    queryset = JenisProdukUMKM.objects.all()
    serializer_class = JenisProdukUMKMSerializer
    permission_classes = [IsSuperAdminOrReadOnly | IsUMKMOrReadOnly]
    
class PermintaanProdukViewSet(ModelViewSet):
    queryset = PermintaanProduk.objects.all()
    serializer_class = PermintaanProdukSerializer
    permission_classes = [IsSuperAdminOrReadOnly | IsUMKMOrReadOnly]
    
class PermintaanPemasokViewSet(ModelViewSet):
    queryset = PermintaanPemasok.objects.all()
    serializer_class = PermintaanPemasokSerializer
    permission_classes = [IsSuperAdminOrReadOnly | IsUMKMOrReadOnly]
    
class PenilaianPemasokViewSet(ModelViewSet):
    queryset = PenilaianPemasok.objects.all()
    serializer_class = PenilaianPemasokSerializer
    permission_classes = [IsSuperAdminOrReadOnly | IsUMKMOrReadOnly]
    
class PrioritasPemasokViewSet(ModelViewSet):
    queryset = PrioritasPemasok.objects.all()
    serializer_class = PrioritasPemasokSerializer
    permission_classes = [IsSuperAdminOrReadOnly | IsUMKMOrReadOnly]
    
class TenagaKerjaViewSet(ModelViewSet):
    queryset = TenagaKerja.objects.all()
    serializer_class = TenagaKerjaSerializer
    permission_classes = [IsSuperAdminOrReadOnly | IsUMKMOrReadOnly]
    
class PerijinanViewSet(ModelViewSet):
    queryset = Perijinan.objects.all()
    serializer_class = PerijinanSerializer
    permission_classes = [IsSuperAdminOrReadOnly | IsUMKMOrReadOnly]
    
class BahanBakuViewSet(ModelViewSet):
    queryset = BahanBaku.objects.all()
    serializer_class = BahanBakuSerializer
    permission_classes = [IsSuperAdminOrReadOnly | IsUMKMOrReadOnly]
    
class PemakaianEnergiViewSet(ModelViewSet):
    queryset = PemakaianEnergi.objects.all()
    serializer_class = PemakaianEnergiSerializer
    permission_classes = [IsSuperAdminOrReadOnly | IsUMKMOrReadOnly]
    
class AlatProduksiViewSet(ModelViewSet):
    queryset = AlatProduksi.objects.all()
    serializer_class = AlatProduksiSerializer
    permission_classes = [IsSuperAdminOrReadOnly | IsUMKMOrReadOnly]
    
class FasilitasViewSet(ModelViewSet):
    queryset = Fasilitas.objects.all()
    serializer_class = FasilitasSerializer
    permission_classes = [IsSuperAdminOrReadOnly | IsUMKMOrReadOnly]

class PelatihanViewSet(ModelViewSet):
    queryset = Pelatihan.objects.all()
    serializer_class = PelatihanSerializer
    permission_classes = [IsSuperAdminOrReadOnly | IsUMKMOrReadOnly]

class LaporanKeuanganViewSet(ModelViewSet):
    queryset = LaporanKeuangan.objects.all()
    serializer_class = LaporanKeuanganSerializer
    permission_classes = [IsAuthenticated | IsSuperAdminOrReadOnly | IsUMKMOrReadOnly | IsKoperasiOrReadOnly]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['nama_KUMKM']
    search_fields = ['nama_KUMKM']
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        
        return Response({"message": "Data deleted successfully"})

class InformasiViewSet(ModelViewSet):
    queryset = Informasi.objects.all()
    serializer_class = InformasiSerializer
    permission_classes = [IsSuperAdminOrReadOnly]
    
class KontakLayananViewSet(ModelViewSet):
    queryset = KontakLayanan.objects.all()
    serializer_class = KontakLayananSerializer        
    permission_classes = [IsSuperAdminOrReadOnly]

class KontakLayananView(APIView):
    def get(self, request, pk):
        try:
            instance = KontakLayanan.objects.get(pk=pk)
            phone_number = instance.wa_nahub

            clean_phone_number = ''.join(filter(str.isdigit, phone_number))

            wa_me_link = f'https://wa.me/{clean_phone_number}'

            return Response({'wa_me_link': wa_me_link}, status=200)
        except KontakLayanan.DoesNotExist:
            return Response({'error': 'Model instance not found.'}, status=404)
        
class PengaduanView(APIView):
    permission_classes = [AllowAny]
    def post(self, request, format=None):
        serializer = PengaduanSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            penerima = "dherasalsabila03@gmail.com"
            subject = data.get('subject')
            pesan = data.get('pesan')
            email = data.get('email')
            serializer.save()
            try:
                send_mail(subject, pesan, email, [penerima], fail_silently=False)
                return Response({'message': 'Email sent successfully!'}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'message': 'Failed to send the email. Please try again later.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GrafikKUMKMView(APIView):
    def get(self, request, format=None):
        koperasi = Koperasi.objects.count()
        umkm = UMKM.objects.count()
        
        labels = ['Koperasi', 'UMKM']
        sizes = np.array([koperasi, umkm])

        if np.isnan(sizes).any():
            return HttpResponse("Data is not available for creating the pie chart.")
                
        plt.figure(figsize=(8, 8))
        plt.pie(sizes.flatten(), labels=labels, autopct='%1.1f%%', startangle=90)
        plt.axis('equal')
        plt.title('Pie Chart')  

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        plt.close()

        buffer.seek(0)
        return HttpResponse(buffer.getvalue(), content_type='image/png')

class KomoditiKUMKM(APIView):
    def get(self, request):
        distinct_komoditi_umkm = JenisProdukUMKM.objects.values_list('komoditi', flat=True)
        distinct_komoditi_koperasi = JenisProdukKoperasi.objects.values_list('komoditi', flat=True)
        
        komoditi_kumkm = list(distinct_komoditi_umkm) + list(distinct_komoditi_koperasi)
        komoditi_counts = Counter(komoditi_kumkm)

        labels = list(komoditi_counts.keys())
        values = list(komoditi_counts.values())

        plt.figure(figsize=(8, 8))
        plt.pie(values, labels=labels)
        plt.title('Komoditi UMKM')
        plt.axis('equal')

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        plt.close()

        buffer.seek(0)
        return HttpResponse(buffer.getvalue(), content_type='image/png')
    
class SkalaUMKM(APIView):
    def get(self, request):
        distinct_skala = UMKM.objects.values_list('skala', flat=True)
        skala_counts = Counter(distinct_skala)
        
        labels = list(skala_counts.keys())
        values = list(skala_counts.values())
        
        plt.figure(figsize=(8, 8))
        x_pos = range(len(labels))
        plt.bar(x_pos, values)
        plt.title('Komoditi UMKM')
        plt.xlabel('Categories')
        plt.ylabel('Values')
        plt.xticks(x_pos, labels)

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        plt.close()

        buffer.seek(0)
        return HttpResponse(buffer.getvalue(), content_type='image/png')
    
class OmzetTertinggi(APIView):
    def get(self, request):
        omzet = UMKM.objects.values_list('omzet', flat=True)
        umkms = UMKM.objects.values_list('nama', flat=True)
        
        x_axis = list(umkms)
        y_axis = list(omzet)
        x_pos = range(len(x_axis))
        
        plt.figure(figsize=(8, 8))
        plt.bar(x_pos, y_axis)
        plt.xlabel('UMKM')
        plt.ylabel('Omzet')
        plt.title('Omzet Tertinggi')
        plt.xticks(x_pos, x_axis)

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        plt.close()

        buffer.seek(0)
        return HttpResponse(buffer.getvalue(), content_type='image/png')

class BullwhipEffectUMKM(APIView):
    def get(self, request, umkm_username):
        foreign_key_value = umkm_username
        queryset = PermintaanProduk.objects.filter(umkm_id=foreign_key_value)

        queryset_produksi = queryset.values_list('nama_produk', 'produksi')
        grouped_data_produksi = {}
        for nama_produk, produksi in queryset_produksi:
            if nama_produk in grouped_data_produksi:
                grouped_data_produksi[nama_produk].append(produksi)
            else:
                grouped_data_produksi[nama_produk] = [produksi]

        queryset_permintaan = queryset.values_list('nama_produk', 'permintaan')
        grouped_data_permintaan = {}
        for nama_produk, permintaan in queryset_permintaan:
            if nama_produk in grouped_data_permintaan:
                grouped_data_permintaan[nama_produk].append(permintaan)
            else:
                grouped_data_permintaan[nama_produk] = [permintaan]
        
        bulan = queryset.values_list('bulan', flat=True).distinct()
        count_bulan = len(bulan)
    
        
        permintaan_by_nama = list(queryset.values('nama_produk').annotate(total_permintaan=Sum('permintaan'), total_produksi=Sum('produksi')))
        par = (1+(2*1/count_bulan)+(1**2/(count_bulan**2)))
        
        be_status = {}
        be_values = []
        nama_list = []
        
        for item in permintaan_by_nama:
            nama = item['nama_produk']
            permintaan = item['total_permintaan']
            produksi = item['total_produksi']
            
            avg_pm = permintaan / count_bulan
            avg_pd = produksi / count_bulan
        
            std_pm = np.std(grouped_data_permintaan[nama], ddof=1)
            std_pd = np.std(grouped_data_produksi[nama], ddof=1)

            koef_pm = std_pm / avg_pm
            koef_pd = std_pd / avg_pd
            
            be = koef_pd / koef_pm
            
            if be > par:
                be_status[nama] = False
            else:
                be_status[nama] = True

            be_values.append(be)
            nama_list.append(nama)
        
        be_values_rounded = [format(be, '.2f') for be in be_values]
        # Plot all Bullwhip Effect values in a single graph
        # plt.bar(nama_list, be_values_rounded, color=[ 'r' if not status else 'b' for status in be_status.values()])
        # plt.axhline(y=par, color='r', linestyle='--')
        # plt.xlabel('Nama')
        # plt.ylabel('Bullwhip Effect (BE) Value')
        # plt.title('Bullwhip Effect berdasarkan Nama Produk')
        # plt.xticks(rotation=45)
        # plt.show() 
        # sorted_data = sorted(zip(be_values_rounded, nama_list))
        # be_values_rounded, nama_list = zip(*sorted_data)
               
        # Draw the horizontal line representing 'par'
        # plt.plot(nama_list, be_values_rounded, marker='o', color='b', label='Bullwhip Effect (BE) Value')
        plt.scatter(nama_list, be_values_rounded, marker='*', color='g', label='Rounded BE Value')
        plt.axhline(y=par, color='r', linestyle='--', label='Parameter')
        plt.text(nama_list[-1], par, f' y = {par}', color='red', ha='right', va='bottom')
        # Customize the plot
        plt.xlabel('Nama')
        plt.ylabel('Bullwhip Effect (BE) Value')
        plt.title('Bullwhip Effect berdasarkan Nama Produk')
        plt.xticks(rotation=45)
        plt.legend()

        # Display the plot
        plt.grid(True)
        plt.show()

        return Response(be_status)
    
class AverageSupplierPerfUMKM(APIView):
    def get(self, request, umkm_username):
        # tabel prioritas
        foreign_key_value = umkm_username
        prioritas_pemasok = PrioritasPemasok.objects.filter(umkm_id=foreign_key_value)
        penilaian_pemasok = PenilaianPemasok.objects.filter(umkm_id=foreign_key_value)
        
        data = {}

        for item in penilaian_pemasok:
            nama = item.nama
            kualitas = item.kualitas
            biaya = item.biaya
            pengiriman = item.pengiriman
        
            for item in prioritas_pemasok:
                kualitas_biaya = item.kualitas_biaya
                kualitas_pengiriman = item.kualitas_pengiriman
                biaya_pengiriman = item.biaya_pengiriman
                
                kb_mapping = {
                    'a': 5, 'b': 4, 'c': 3, 'd': 2, 'e': 1, 'f': 1/2, 'g': 1/3, 'h': 1/4, 'i': 1/5
                }
                kp_mapping = {
                    'a': 5, 'b': 4, 'c': 3, 'd': 2, 'e': 1, 'f': 1/2, 'g': 1/3, 'h': 1/4, 'i': 1/5
                }
                bp_mapping = {
                    'a': 5, 'b': 4, 'c': 3, 'd': 2, 'e': 1, 'f': 1/2, 'g': 1/3, 'h': 1/4, 'i': 1/5
                }
                
                kk, bb, pp = 1, 1, 1
                
                kb_value = kb_mapping.get(kualitas_biaya, 1)
                kp_value = kp_mapping.get(kualitas_pengiriman, 1)
                bp_value = bp_mapping.get(biaya_pengiriman, 1)
                
                row1 = [kk, kb_value, kp_value]
                row2 = [1/kb_value, bb, bp_value]
                row3 = [1/kp_value, 1/bp_value, pp]
                
                sum_row1 = sum(row1)
                sum_row2 = sum(row2)
                sum_row3 = sum(row3)
                
                bobot1 = sum_row1 / 3
                bobot2 = sum_row2 / 3
                bobot3 = sum_row3 / 3
                
                nilai_kualitas = kualitas * bobot1
                nilai_biaya = biaya * bobot2
                nilai_pengiriman = pengiriman * bobot3
                total_nilai = nilai_kualitas + nilai_biaya + nilai_pengiriman
                
                data[nama] = total_nilai
                break
           
        nama_list = []
        total_nilai_list = []
        for nama, total_nilai in data.items():
            nama_list.append(nama)
            total_nilai_list.append(total_nilai)
        positions = range(len(nama_list))
            
        plt.bar(nama_list, total_nilai_list)
        plt.xlabel('Nama')
        plt.ylabel('Total Nilai')
        plt.title('Total Nilai by Nama')
        plt.xticks(positions, nama_list)
        plt.show()
               
        return Response(data)