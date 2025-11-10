from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def example_view(request):
    return Response({"mensaje": "Hola desde Django!"}, status=status.HTTP_200_OK)



