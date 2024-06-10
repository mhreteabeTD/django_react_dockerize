from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def my_view(request):
    return Response({'message': 'Hello, world from backend!'})

