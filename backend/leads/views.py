from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from .models import Lead
from .serializers import LeadSerializer, LeadCreateSerializer, LeadUpdateSerializer
from clients.models import Client

class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action == 'create':
            return LeadCreateSerializer
        if self.action in ['update', 'partial_update']:
            return LeadUpdateSerializer
        return LeadSerializer

    def perform_create(self, serializer):
        # Auto-assign if not specified, or other logic
        serializer.save()

    @action(detail=True, methods=['post'], url_path='assign')
    def assign_lead(self, request, pk=None):
        lead = self.get_object()
        user_id = request.data.get('user_id')
        if not user_id:
            return Response({'error': 'User ID required'}, status=status.HTTP_400_BAD_REQUEST)
        
        lead.assigned_to_id = user_id
        lead.save()
        return Response({'status': 'lead assigned'})

    @action(detail=True, methods=['post'], url_path='convert')
    def convert_to_client(self, request, pk=None):
        lead = self.get_object()
        
        if lead.status == 'converted':
            return Response({'error': 'Lead already converted'}, status=status.HTTP_400_BAD_REQUEST)
            
        # Create Client from Lead
        client = Client.objects.create(
            name=lead.name,
            email=lead.email,
            phone=lead.phone,
            company=lead.company,
            converted_from_lead=lead,
            account_manager=lead.assigned_to, # Assign to lead owner by default
            notes=f"Converted from lead on {timezone.now()}"
        )
        
        lead.status = 'converted'
        lead.save()
        
        return Response({'status': 'converted to client', 'client_id': client.id})

    @action(detail=True, methods=['post'], url_path='add-comment')
    def add_comment(self, request, pk=None):
        lead = self.get_object()
        comment = request.data.get('comment')
        if not comment:
            return Response({'error': 'Comment required'}, status=status.HTTP_400_BAD_REQUEST)
        
        timestamp = timezone.now().strftime("%Y-%m-%d %H:%M")
        user = request.user.get_full_name()
        new_note = f"\n[{timestamp}] {user}: {comment}"
        
        lead.notes = (lead.notes or "") + new_note
        lead.save()
        return Response({'status': 'comment added'})
