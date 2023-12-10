from rest_framework import routers
from .views import BeritaViewSet, FaktaViewSet, ProdukHukumViewSet, RapatKoordinasiViewSet, PaparanViewSet, KoperasiViewSet, UMKMViewSet, LaporanKeuanganViewSet, GambarViewSet, RegisterViewSet, ChangePasswordViewSet, InformasiViewSet, KontakLayananViewSet

router = routers.SimpleRouter()
router.register(r'news', BeritaViewSet, basename='news')
router.register(r'fact', FaktaViewSet, basename='fact')
router.register(r'regulation/coor-meeting', RapatKoordinasiViewSet, basename='regulation/coor-meeting')
router.register(r'regulation/product-of-law', ProdukHukumViewSet, basename='regulation/product-of-law')
router.register(r'regulation/exposure', PaparanViewSet, basename='regulation/exposure')
router.register(r'koperasi', KoperasiViewSet, basename='koperasi')
router.register(r'umkm', UMKMViewSet, basename='umkm')
router.register(r'financial', LaporanKeuanganViewSet, basename='financial')
# router.register(r'gallery', GambarViewSet, basename='gallery')
router.register(r'account', RegisterViewSet, basename='account')
router.register(r'change-password', ChangePasswordViewSet, basename='change-password')
router.register(r'information', InformasiViewSet, basename='information')
router.register(r'contact-us', KontakLayananViewSet, basename='contact-us')

urlpatterns = [
    # path('', ForgotPasswordFormView.as_view()),
]

urlpatterns += router.urls