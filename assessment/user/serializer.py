from rest_framework import serializers
from datetime import datetime

class ItemSerializer(serializers.Serializer):
    item_id = serializers.CharField(max_length=100, required = True)
    quantity = serializers.IntegerField(min_value=1, required = True)
    price = serializers.FloatField (min_value=0.01, required = True)
    
class RequestSerializer(serializers.Serializer):
    user_id = serializers.CharField(max_length=100, required = True)
    email = serializers.EmailField(required = True)
    timestamp = serializers.CharField(required = True)
    items = ItemSerializer(many=True)
    
    def validate_timestamp(self, value):
        try:
            datetime.strptime(value, "%Y-%m-%d%H:%M:%SZ")
            return value
        except ValueError:
            raise serializers.ValidationError("TimeStamp not valid")
        
    def validate_items(self, value):
        if not value:
            raise serializers.ValidationError("Item list cannot be null")
        return value
    
    