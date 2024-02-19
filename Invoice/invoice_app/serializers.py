from rest_framework import serializers
from .models import *
        

class InvoiceDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = InvoiceDetail
        fields = ['id','invoice','description', 'quantity', 'unit_price', 'price']
        # fields = '__all__'
   
   
class InvoiceSerializer(serializers.ModelSerializer):
    invoice_detail = InvoiceDetailSerializer(many=True,read_only = True)
    class Meta:
        model = Invoice
        fields = ['id', 'date', 'customer_name', 'invoice_detail']
        
    def create(self,validated_data):
        invoice_details_data = validated_data.pop('invoice_detail',[])
        invoice  = Invoice.objects.create(**validated_data)
        for detail_data in invoice_details_data:
            detail_data['invoice'] = invoice
            InvoiceDetail.objects.create(invoice=invoice,  **detail_data)
        return invoice
        
    def update(self,instance,validated_data):
        invoice_details_data = validated_data.pop('invoice_detail',[])
        # instance = super().update(instance,validate_data)
        instance.date = validated_data.get('date', instance.date)
        instance.customer_name = validated_data.get('customer_name', instance.customer_name)
        instance.save()
        
        existing_invoice_details = {invoice_detail.id : invoice_detail for invoice_detail in instance.invoice_detail.all()}
        for detail_data in invoice_details_data:
            detail_id = detail_data.get('id')
            if detail_id in existing_invoice_details:
                detail = existing_invoice_details.pop(detail_id)
                for attr,value in detail_data.items():
                    setattr(detail, attr, value)
                detail.save()
            else:
                InvoiceDetail.objects.create(invoice=instance, **detail_data )
                
        
        # for detail in existing_invoice_details.values():
        #     detail.delete()
            
        return instance
            
            
            