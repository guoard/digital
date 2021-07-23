from rest_framework import serializers
from .models import Mobile, HandsFree, Seller


class SellerField(serializers.RelatedField):
    def to_representation(self, value):
        return value.name


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        exclude = ['id']


class MobileSerializer(serializers.ModelSerializer):
    seller = SellerSerializer()

    class Meta:
        model = Mobile
        fields = '__all__'

    def create(self, validated_data):
        seller_validated_data = validated_data.pop('seller')
        seller = Seller.objects.create(**seller_validated_data)
        validated_data['seller'] = seller
        mobile = Mobile.objects.create(**validated_data)
        return mobile


class HandsFreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HandsFree
        fields = '__all__'
