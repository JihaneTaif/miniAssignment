from rest_framework import serializers
from .models import Lead
from users.serializers import UserSerializer


class LeadSerializer(serializers.ModelSerializer):
    """Serializer for Lead model with nested user info"""
    assigned_to_detail = UserSerializer(source='assigned_to', read_only=True)
    
    class Meta:
        model = Lead
        fields = ['id', 'name', 'email', 'phone', 'company', 'status', 'source',
                  'assigned_to', 'assigned_to_detail', 'notes', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class LeadCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating leads"""
    
    class Meta:
        model = Lead
        fields = ['name', 'email', 'phone', 'company', 'source', 'assigned_to', 'notes']


class LeadUpdateSerializer(serializers.ModelSerializer):
    """Serializer for updating leads"""
    
    class Meta:
        model = Lead
        fields = ['name', 'email', 'phone', 'company', 'status', 'source', 'assigned_to', 'notes']
