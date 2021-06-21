from clinics.models import Clinic, Doctor, Specialty
from rest_framework import serializers


class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctor
        fields = ['first_name', 'last_name', 'clinic', 'specialty']


class ClinicSerializer(serializers.HyperlinkedModelSerializer):
    doctors = DoctorSerializer(many=True, read_only=True)

    class Meta:
        model = Clinic
        fields = ['name', 'street_address', 'city', 'state', 'doctors']

class SpecialtySerializer(serializers.HyperlinkedModelSerializer):
    doctors = DoctorSerializer(many=True, read_only=True)

    class Meta:
        model = Specialty
        fields = ['specialty_title', 'doctors']
