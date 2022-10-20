from rest_framework import serializers
from .models import Country

# build dumb 
class CountrySerializer(serializers.ModelSerializer):
    class Meta:

        model = Country
        fields = ["id", "name", "capital", "area"]