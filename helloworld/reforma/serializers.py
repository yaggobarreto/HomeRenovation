from rest_framework import serializers

from .models import ReformaItem


class ReformaItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReformaItem
        fields = '__all__'
