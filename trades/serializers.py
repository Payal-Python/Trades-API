from rest_framework import serializers
from .models import Trade

class TradeSerializer(serializers.ModelSerializer):
    trader = serializers.CharField(source='trader.username', read_only=True)

    class Meta:
        model = Trade
        fields = ['id', 'trader', 'trade_type', 'symbol', 'quantity', 'price', 'executed_at', 'notes']
        read_only_fields = ['id', 'trader', 'executed_at']
