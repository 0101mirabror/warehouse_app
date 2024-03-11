from rest_framework import serializers
from coreapp.models import *


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materials
        fields = ('id', 'material_name')
    
class ProductMaterialSerializer(serializers.ModelSerializer):
    material = MaterialSerializer()
    class Meta:
        model = ProductMaterials
        fields = ('id', 'product_id', 'material_id', 'quantity', 'material')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'