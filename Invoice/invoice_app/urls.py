from django.urls import path
from .views import *

urlpatterns = [
   
    path('invoices/', InvoiceListCreate.as_view(), name='invoice-list'),
    path('invoices/<int:pk>/',InvoiceRetriveUpdateDestroy.as_view(), name= 'invoice-detail'),
    path('invoices/<int:invoice_pk>/details/', InvoiceDetailListCreate.as_view(), name='invoice-detail-list-create'),
    path('invoices/<int:invoice_pk>/details/<int:pk>/', InvoiceDetailRetrieveUpdateDestroy.as_view(), name='invoice-detail-detail'),
]
