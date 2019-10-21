"""Rutas del módulo de ordenes de venta
"""
# Django Library
from django.urls import path

# Localfolder Library
from ..reports.invoicepdf import invoice_pdf
from ..views import (
    InvoiceAddView, InvoiceDeleteView, InvoiceDetailView, InvoiceEditView,
    InvoiceListView, invoice_active, invoice_state, load_product, load_tax)

app_name = 'PyInvoice'

urlpatterns = [
    # =========================== Invoice URL's ============================ #
    path('', InvoiceListView.as_view(), name='list'),
    path('<int:pk>', InvoiceDetailView.as_view(), name='detail'),
    path('add/', InvoiceAddView.as_view(), name='add'),
    path('<int:pk>/edit/', InvoiceEditView.as_view(), name='update'),
    path('<int:pk>/delete/', InvoiceDeleteView.as_view(), name='delete'),
    path('state/<int:pk>/<int:state>', invoice_state, name='state'),
    path('active/<int:pk>/<int:active>', invoice_active, name='active'),

    # ======================== Invoice= AJAX URL's ========================= #
    path('load-product/', load_product, name='ajax_load_product'),
    path('load-tax/', load_tax, name='ajax_load_tax'),

    # ====================== Invoice= Reports URL's ======================== #
    path(
        'pdf/<int:pk>',
        invoice_pdf,
        name='pdf'
    ),
]
