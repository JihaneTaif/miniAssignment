from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from .models import Claim
from .serializers import ClaimSerializer, ClaimCreateSerializer, ClaimUpdateSerializer


class ClaimViewSet(viewsets.ModelViewSet):
    queryset = Claim.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action == 'create':
            return ClaimCreateSerializer
        if self.action in ['update', 'partial_update']:
            return ClaimUpdateSerializer
        return ClaimSerializer

    def get_queryset(self):
        queryset = Claim.objects.all()
        
        # Filter by status
        claim_status = self.request.query_params.get('status', None)
        if claim_status:
            queryset = queryset.filter(status=claim_status)
        
        # Filter by client
        client_id = self.request.query_params.get('client', None)
        if client_id:
            queryset = queryset.filter(client_id=client_id)
        
        # Filter by assigned user
        assigned_to = self.request.query_params.get('assigned_to', None)
        if assigned_to:
            queryset = queryset.filter(assigned_to_id=assigned_to)
        
        return queryset

    @action(detail=True, methods=['post'], url_path='assign')
    def assign_claim(self, request, pk=None):
        claim = self.get_object()
        user_id = request.data.get('user_id')
        
        if not user_id:
            return Response({'error': 'User ID required'}, status=status.HTTP_400_BAD_REQUEST)
        
        claim.assigned_to_id = user_id
        if claim.status == 'open':
            claim.status = 'in_progress'
        claim.save()
        
        return Response({'status': 'claim assigned'})

    @action(detail=True, methods=['post'], url_path='resolve')
    def resolve_claim(self, request, pk=None):
        claim = self.get_object()
        resolution_notes = request.data.get('resolution_notes', '')
        
        claim.status = 'resolved'
        claim.resolution_notes = resolution_notes
        claim.resolved_at = timezone.now()
        claim.save()
        
        return Response({'status': 'claim resolved'})

    @action(detail=True, methods=['post'], url_path='add-comment')
    def add_comment(self, request, pk=None):
        claim = self.get_object()
        comment = request.data.get('comment')
        
        if not comment:
            return Response({'error': 'Comment required'}, status=status.HTTP_400_BAD_REQUEST)
        
        timestamp = timezone.now().strftime("%Y-%m-%d %H:%M")
        user = request.user.get_full_name()
        new_note = f"\n[{timestamp}] {user}: {comment}"
        
        claim.resolution_notes = (claim.resolution_notes or "") + new_note
        claim.save()
        
        return Response({'status': 'comment added'})

    @action(detail=True, methods=['post'], url_path='update-status')
    def update_status(self, request, pk=None):
        claim = self.get_object()
        new_status = request.data.get('status')
        
        if new_status not in dict(Claim.STATUS_CHOICES):
            return Response({'error': 'Invalid status'}, status=status.HTTP_400_BAD_REQUEST)
        
        claim.status = new_status
        
        if new_status == 'resolved' and not claim.resolved_at:
            claim.resolved_at = timezone.now()
        
        claim.save()
        
        return Response({'status': 'claim status updated'})
