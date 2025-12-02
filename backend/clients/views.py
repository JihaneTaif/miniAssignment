from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum, Count
from .models import Client
from .serializers import ClientSerializer, ClientCreateSerializer, ClientListSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action == 'create':
            return ClientCreateSerializer
        if self.action == 'list':
            return ClientListSerializer
        return ClientSerializer

    def get_queryset(self):
        queryset = Client.objects.all()
        # Filter by account manager if specified
        account_manager = self.request.query_params.get('account_manager', None)
        if account_manager:
            queryset = queryset.filter(account_manager_id=account_manager)
        return queryset

    @action(detail=True, methods=['post'], url_path='assign-products')
    def assign_products(self, request, pk=None):
        client = self.get_object()
        product_ids = request.data.get('product_ids', [])
        
        # This would require a many-to-many relationship or separate model
        # For now, we'll just acknowledge the request
        return Response({'status': 'products assigned', 'product_ids': product_ids})

    @action(detail=True, methods=['get'], url_path='total-income')
    def total_income(self, request, pk=None):
        client = self.get_object()
        
        # This would calculate based on orders/invoices
        # For now, return a placeholder
        total = 0  # Would sum from related orders/invoices
        
        return Response({'client_id': client.id, 'total_income': total})

    @action(detail=True, methods=['get'], url_path='activity-history')
    def activity_history(self, request, pk=None):
        client = self.get_object()
        
        # Get related claims count
        claims_count = client.claims.count()
        
        history = {
            'client_id': client.id,
            'created_at': client.created_at,
            'total_claims': claims_count,
            'converted_from_lead': client.converted_from_lead_id is not None,
            'notes': client.notes
        }
        
        return Response(history)
