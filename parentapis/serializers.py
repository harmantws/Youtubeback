from rest_framework import serializers
from .models import NotAllowedSearches

class NotAllowedSearchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotAllowedSearches
        fields = ['searches', 'created_at']