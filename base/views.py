from django.shortcuts import render
import requests
import json
import mysql.connector
from mysql.connector import Error
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Inventory, Supplier
from .serializers import InventorySerializer, SupplierSerializer
from online_store_api import settings

# Create your views here.

# Routes information
@api_view(['GET']) 
def getRoutes(request):

    routes = [
        'GET /api/inventory_list/',
        'GET /api/supplier_list/',
        'POST /api/add_inventory_item/',
        'POST /api/add_supplier/',
        'POST /api/update_inventory_item/',
        'POST /api/update_supplier/',
        'DELETE /api/delete_inventory_item/',
        'DELETE /api/delete_supplier/',
    ]
    return Response(routes)

# view inventory items
@api_view(['GET'])
def getInventory(request):

    supplier = request.GET.get('supplier', False)
    name = request.GET.get('name', False)

    if supplier:
      try:
          Inventory.objects.filter(supplier_id=supplier)
      except Inventory.DoesNotExist:
          return Response({"status": "error", "message": "data not found"}, status=status.HTTP_404_NOT_FOUND)

      vendor = Inventory.objects.filter(supplier_id=supplier)
      serializer = InventorySerializer(vendor, many=True)
      return Response(serializer.data)
    elif name:
        try:
          Inventory.objects.filter(name__contains=name)
        except Inventory.DoesNotExist:
          return Response({"status": "error", "message": "data not found"}, status=status.HTTP_404_NOT_FOUND)

        item = Inventory.objects.filter(name__contains=name)
        serializer = InventorySerializer(item, many=True)
        return Response(serializer.data)
    else:
        inventory = Inventory.objects.all()
        serializer = InventorySerializer(inventory, many=True)
        return Response(serializer.data)

# view supplier
@api_view(['GET'])
def getSupplier(request):

    name = request.GET.get('name', False)

    if name:
       
       try:
          Supplier.objects.filter(name__contains=name)
       except Supplier.DoesNotExist:
          return Response({"status": "error", "message": "data not found"}, status=status.HTTP_404_NOT_FOUND)

       vendor = Supplier.objects.filter(name__contains=name)
       serializer = SupplierSerializer(vendor, many=True)
       return Response(serializer.data)
    
    else:
        inventory = Supplier.objects.all()
        serializer = SupplierSerializer(inventory, many=True)
        return Response(serializer.data)

# add inventory item
@api_view(['POST'])
def addItem(request):

    # validating for already existing data
    if Inventory.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    item = InventorySerializer(data=request.data)

    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response({"status": "error", "data": item.errors}, status=status.HTTP_400_BAD_REQUEST)

# add supplier
@api_view(['POST'])
def addSupplier(request):

    # validating for already existing data
    if Supplier.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    vendor = SupplierSerializer(data=request.data)

    if vendor.is_valid():
        vendor.save()
        return Response(vendor.data)
    else:
        return Response({"status": "error", "data": vendor.errors}, status=status.HTTP_400_BAD_REQUEST)

# update inventory item
@api_view(['POST'])
def updateItem(request, pk):
    item = Inventory.objects.get(id=pk)
    info = InventorySerializer(item, data = request.data, partial=True)

    if info.is_valid():
        info.save()
        return Response(info.data)
    else:
        return Response({"status": "error", "data": info.errors}, status=status.HTTP_400_BAD_REQUEST)

# update supplier
@api_view(['POST'])
def updateSupplier(request, pk):
    vendor = Supplier.objects.get(id=pk)
    info = SupplierSerializer(vendor, data = request.data, partial=True)

    if info.is_valid():
        info.save()
        return Response(info.data)
    else:
        return Response({"status": "error", "data": info.errors}, status=status.HTTP_400_BAD_REQUEST)

# delete inventory item
@api_view(['DELETE'])
def deleteItem(request, pk=None):
    item = get_object_or_404(Inventory, id=pk)
    item.delete()
    return Response({"status": "success", "data": "Record Deleted"}, status=status.HTTP_202_ACCEPTED)

# delete supplier
@api_view(['DELETE'])
def deleteSupplier(request, pk=None):
    item = get_object_or_404(Supplier, id=pk)
    item.delete()
    return Response({"status": "success", "data": "Record Deleted"}, status=status.HTTP_202_ACCEPTED)