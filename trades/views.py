from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .models import Trade
from .serializers import TradeSerializer

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions for authenticated users, write only for owner/trader
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.trader == request.user

class TradeViewSet(viewsets.ModelViewSet):
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(trader=self.request.user)
