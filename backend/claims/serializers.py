from rest_framework import serializers
from .models import Claim
from users.serializers import UserSerializer
from clients.serializers import ClientListSerializer
from products.serializers import ProductSerializer


class ClaimSerializer(serializers.ModelSerializer):
    """Serializer for Claim model with nested details"""
    client_detail = ClientListSerializer(source='client', read_only=True)
    product_detail = ProductSerializer(source='product', read_only=True)
    assigned_to_detail = UserSerializer(source='assigned_to', read_only=True)
    
    class Meta:
        model = Claim
        fields = ['id', 'client', 'client_detail', 'product', 'product_detail',
                  'assigned_to', 'assigned_to_detail', 'title', 'description',
                  'status', 'priority', 'resolution_notes', 'created_at', 
                  'updated_at', 'resolved_at']
        read_only_fields = ['id', 'created_at', 'updated_at', 'resolved_at']


class ClaimCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating claims"""
    
    class Meta:
        model = Claim
        fields = ['client', 'product', 'title', 'description', 'priority']


class ClaimUpdateSerializer(serializers.ModelSerializer):
    """Serializer for updating claims"""
    
    class Meta:
        model = Claim
        fields = ['status', 'priority', 'assigned_to', 'resolution_notes']
