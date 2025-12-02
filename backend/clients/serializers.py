from rest_framework import serializers
from .models import Client
from users.serializers import UserSerializer
from leads.serializers import LeadSerializer


class ClientSerializer(serializers.ModelSerializer):
    """Serializer for Client model with nested relations"""
    account_manager_detail = UserSerializer(source='account_manager', read_only=True)
    converted_from_lead_detail = LeadSerializer(source='converted_from_lead', read_only=True)
    
    class Meta:
        model = Client
        fields = ['id', 'name', 'email', 'phone', 'company', 'address', 'industry',
                  'account_manager', 'account_manager_detail', 'converted_from_lead',
                  'converted_from_lead_detail', 'notes', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class ClientCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating clients"""
    
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone', 'company', 'address', 'industry',
                  'account_manager', 'converted_from_lead', 'notes']


class ClientListSerializer(serializers.ModelSerializer):
    """Simplified serializer for client lists"""
    account_manager_name = serializers.CharField(source='account_manager.get_full_name', read_only=True)
    
    class Meta:
        model = Client
        fields = ['id', 'name', 'email', 'company', 'account_manager_name', 'created_at']
