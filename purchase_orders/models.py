from django.db import models
from django.utils import timezone
from vendors.models import Vendor
from purchase_orders.constants import PO_STATUS_CHOICES

class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=100, unique=True, help_text="Unique number identifying the PO.")
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField(default=timezone.now, help_text="Date when the order was placed.")
    delivery_date = models.DateTimeField(help_text="Expected or actual delivery date of the order.")
    items = models.JSONField(help_text="Details of items ordered.")
    quantity = models.IntegerField(help_text="Total quantity of items in the PO.")
    status = models.CharField(max_length=20, choices=PO_STATUS_CHOICES,
        help_text="Current status of the PO")
    quality_rating = models.FloatField(null=True, help_text="Rating given to the vendor for this PO.")
    issue_date = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the PO was issued to the vendor.")
    acknowledgment_date = models.DateTimeField(null=True, help_text="Timestamp when the vendor acknowledged the PO.")

    def __str__(self) -> str:
        return f'PO-{self.po_number}'
    
    def save(self, *args, **kwargs):
        if self.status == 'completed' and not self.delivery_date:
            self.delivery_date = timezone.now()
        if self.status == 'completed' and not self.issue_date:
            self.issue_date = timezone.now()
            
        completed_orders = self.vendor.purchaseorder_set.filter(status='complete')
        if self.pk is not None:  # If the object already exists
            old_order_obj = PurchaseOrder.objects.get(pk=self.pk)
            if self.status != old_order_obj.status:
                self.vendor.fulfillment_rate_calculator()
            if self.status == 'completed' and old_order_obj.status != 'completed':
                self.vendor.on_time_delivery_calculator(completed_orders)
            if self.acknowledgment_date != old_order_obj.acknowledgment_date:
                self.vendor.average_response_time_calculator()
            if self.status == 'completed' and old_order_obj.status != 'completed' and self.quality_rating is not None:
                self.vendor.quality_rating_avg_calculator(completed_orders)
        super().save(*args, **kwargs)
        
        
    
            
        
            
            
        
            
