from clinics.models import Clinic, Doctor, Specialty
from rest_framework import viewsets
from clinics.serializers import ClinicSerializer, DoctorSerializer, SpecialtySerializer


class ClinicViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Clinics
    """
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Clinics
    """
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class SpecialtyViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Clinics
    """
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer