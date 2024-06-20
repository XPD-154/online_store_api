from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('api/inventory_list/', views.getInventory),
    path('api/supplier_list/', views.getSupplier),
    path('api/add_inventory_item/', views.addItem),
    path('api/add_supplier/', views.addSupplier),
    path('api/update_inventory_item/<str:pk>', views.updateItem),
    path('api/update_supplier/<str:pk>', views.updateSupplier),
    path('api/delete_inventory_item/<str:pk>', views.deleteItem),
    path('api/delete_supplier/<str:pk>', views.deleteSupplier),
]
