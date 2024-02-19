from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
# Create your views here.


class InvoiceListCreate(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    
class InvoiceRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset=Invoice.objects.all()
    serializer_class=InvoiceSerializer
    
class InvoiceDetailListCreate(generics.ListCreateAPIView):
    
    serializer_class = InvoiceDetailSerializer
    
    def get_queryset(self):
        pk = self.kwargs.get('invoice_pk')
        return InvoiceDetail.objects.filter(invoice_id = pk)

class InvoiceDetailRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Invoice.objects.all()
    serializer_class=InvoiceDetailSerializer
     
    def get_queryset(self):
        # invoice_pk = self.kwargs.get('invoice_pk')
        pk = self.kwargs['pk']
        return InvoiceDetail.objects.filter(id=pk)