''' serializers convert complex data types like Django QuerySets
and model instances into JSON for API responses and deserialize 
incoming data to ensure it meets validation rules before saving 
it to the database. They streamline data conversion, validation
and customization, making API development more efficient and structured. '''

from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'