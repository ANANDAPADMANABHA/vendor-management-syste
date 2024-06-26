from rest_framework import serializers
from .models import PurchaseOrder

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = ['id', 'po_number', 'vendor', 'vendor', 'order_date','delivery_date', 'items','quantity','status','quality_rating','issue_date','acknowledgment_date']
