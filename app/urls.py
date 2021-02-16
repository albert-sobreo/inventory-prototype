from app.views.restjson import getSidebarBranchData
from app.views.vc import customers_save_process, vendors_save_process
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
    path('deliverynotapproved/', views.sales_notapproved),
    path('logs/in/', views.purchaseLogsView),
    path('logs/out/', views.salesLogsView),
    path('logs/transfer/', views.transferLogsView),
    path('logs/spoilage/', views.spoilageLogsView),
    path('sales/approved/', views.sales_approved),
    path('sales/notapproved/', views.sales_notapproved),
    path('purchase/notapproved/', views.purchase_notapproved),
    path('purchase/approved/', views.purchase_approved),
    path('getpurchasemodaldata/', views.getPurchaseModalData),
    path('getsalesmodaldata/', views.getSalesModalData),
    path('approvepurchase/', views.approvePurchase),
    path('approvesales/', views.approveSales),
    path('vendor/', views.vendors_page),
    path('customer/', views.customers_page),
    path('vendorsaveprocess/', views.vendors_save_process),
    path('customersaveprocess/', views.customers_save_process),
    path('getvendormodaldata/', views.getVendorModalData),
    path('getcustomermodaldata/', views.getCustomerModalData),
    path('reports/costofgoodsold/', views.costOfGoodSold),
    path('transfer/approved/', views.transfer_approved),
    path('transfer/notapproved/', views.transfer_notapproved),
    path('spoilage/notapproved/', views.spoilage_notapproved),
    path('spoilage/approved/', views.spoilage_approved),
    path('gettransfermodaldata/', views.getTransferModalData),
    path('getspoilagemodaldata/', views.getSpoilageModalData),
    path('approvetransfer/', views.approveTransfer),
    path('approvespoilage/', views.approveSpoilage),
    path('top-level/branch/<str:pk_branch>/inventory/', views.topLevelBranchInvnetory),
    path('top-level/home/', views.topLevelHome),
    path('getsidebarbranchdata/', views.getSidebarBranchData),
    path('top-level/Customers/', views.topLevelCustomers),
    path('top-level/Suppliers/', views.topLevelSuppliers),
    path('top-level/Purchase/', views.topLevelPurchase),
    path('top-level/Sales/', views.topLevelSales),
    path('top-level/Transfers/', views.topLevelTransfers),
    path('top-level/Spoilage/', views.topLevelSpoilage),
    path('top-level/Approvals/', views.topLevelApprovals),
]
