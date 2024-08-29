from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view,auhtentication_classes,permission_classes
# from rest_framework.response import Response
# from rest_framework import status
# from django.core.paginator import Paginator
# from django.db.models import Q
from .serializers import PropertyListSerializer
from models import Property

@api_view(['GET'])
@auhtentication_classes([])
@permkission_classes([])
def property_list(request):
    if request.method == 'GET':
        properties = Property.objects.all()
        serializer = PropertyListSerializer(properties, many=True)
        return JsonResponse(serializer.data, safe=False)