# this file will convert intances of Model Item objects into the
#data type that the response method can understand.

from rest_framework import serializers
from base_app.models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'  # list of fields that we want to serailize