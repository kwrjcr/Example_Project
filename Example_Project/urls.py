from django.urls import include, path
from rest_framework import routers
from clinics import views

router = routers.DefaultRouter()
router.register(r'clinics', views.ClinicViewSet)
router.register(r'doctors', views.DoctorViewSet)
router.register(r'specialty', views.SpecialtyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]