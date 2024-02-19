from django.db import models

# Create your models here.

class Invoice(models.Model):
    date = models.DateField()
    customer_name = models.CharField(max_length =50)
    
    def __str__(self):
        return str(self.customer_name)
    

class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(Invoice,on_delete=models.CASCADE, related_name = "invoice_detail")
    description = models.CharField(max_length = 200)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits = 8,decimal_places = 2)
    price = models.DecimalField(max_digits = 8,decimal_places=2)
    
    
    def __str__(self):
        return str(self.invoice)
    


