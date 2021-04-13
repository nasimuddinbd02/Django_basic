from rest_framework import serializers
from .models import Brand, Category,Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

    def create(self, validated_data):
        return Category.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
       instance.Save()
       return instance

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields='__all__'

    def create(self, validated_data):
        return Brand.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
       instance.Save()
       return instance


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'
    
    def create(self, validated_data):
        return Product.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
       instance.Save()
       return instance
        
