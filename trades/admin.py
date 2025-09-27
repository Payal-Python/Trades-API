from django.contrib import admin
from .models import Trade

@admin.register(Trade)
class TradeAdmin(admin.ModelAdmin):
    list_display = ('id', 'trade_type', 'symbol', 'quantity', 'price', 'executed_at', 'trader')
    list_filter = ('trade_type', 'symbol')
    search_fields = ('symbol',)
