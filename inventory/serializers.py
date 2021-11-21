from rest_framework.serializers import ModelSerializer
from inventory.models import Product

class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ('id','ProductName','ProductDesc','is_stockable',)
