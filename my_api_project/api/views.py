from encodings import search_function
from rest_framework.response import Response
from rest_framework.decorators import api_view
from base_app.models import Item
from .serializers import ItemSerializer


@api_view(['Get'])
def getData(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)  #many tells to serialize multiple items,
    return Response(serializer.data)


@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid(): # checking if the passed data is valid
        serializer.save()
    return Response(serializer.data)