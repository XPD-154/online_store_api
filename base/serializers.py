from rest_framework.serializers import ModelSerializer
from .models import Inventory, Supplier

# inventory serializer
class InventorySerializer(ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'

#supplier serializer
class SupplierSerializer(ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'