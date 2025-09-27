from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Trade(models.Model):
    TRADE_TYPES = (('BUY', 'Buy'), ('SELL', 'Sell'))

    id = models.AutoField(primary_key=True)
    trader = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    trade_type = models.CharField(max_length=4, choices=TRADE_TYPES)
    symbol = models.CharField(max_length=20)
    quantity = models.DecimalField(max_digits=20, decimal_places=4)
    price = models.DecimalField(max_digits=20, decimal_places=4)
    executed_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, default='')

    class Meta:
        ordering = ['-executed_at']

    def __str__(self):
        return f"{self.trade_type} {self.symbol} @{self.price} x{self.quantity}"
