from django.urls import path
from api.views import MyObtainTokenPairView, LogoutView, SkalaUMKM, KomoditiKUMKM, BullwhipEffectUMKM, AverageSupplierPerfUMKM, MarkersMapView, PengaduanView, KontakLayananView
urlpatterns = [
     path('login/', MyObtainTokenPairView.as_view(), name='login'),
     path('logout/', LogoutView.as_view(), name='logout'),
     path("map/", MarkersMapView.as_view()),
     path('skala/', SkalaUMKM.as_view()),
     path('komoditi/', KomoditiKUMKM.as_view()),
     path('be/<str:umkm_username>/', BullwhipEffectUMKM.as_view()),
     path('avg/<str:umkm_username>/', AverageSupplierPerfUMKM.as_view()),
     path('send-email/', PengaduanView.as_view()),
     path('contact-us/contact-person/<int:pk>/', KontakLayananView.as_view()),
]