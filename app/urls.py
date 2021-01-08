from app.views.sales import outView
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login),
    path('loginprocess/', views.loginprocess),
    path('logout/', views.logout),
    path('register/', views.register),
    path('registerprocess/', views.registerprocess),
    path('inventory-page/', views.inventory_page),
    path('warehouse-save-process/', views.warehouse_save_process),
    path('', views.warehouse_list),
    path('warehouse-edit/', views.warehouse_edit),
    path('warehouse-edit-save/', views.warehouse_edit_save),
    path('inventory-save-process/', views.inventory_save_process),
    path('inventory-delete/', views.inventory_delete),
    path('inventory-edit/', views.inventory_edit),
    path('inventory-edit-save/', views.inventory_edit_save),
    path('test-success/', views.test_success),
    path('test-error', views.test_error),
    path('test-warning', views.test_warning),
    path('test-info', views.test_info),
    #path('temp-po/', views.po),
    #path('po-process/', views.poProcess),
    path('in/', views.inView),
    path('out/', views.outView),
    path('getitemremaining/', views.getItemRemaining),
    path('purchaseprocess/', views.purchaseProcess),
    path('salesprocess/', views.salesProcess),
    path('transfer/', views.transferView),
    path('transferprocess/', views.transferProcess),
    path('spoilage/', views.spoilageView),
    path('spoilageprocess/', views.spoilageProcess),
    path('deliverynotapproved/', views.sales_notapproved)
]
