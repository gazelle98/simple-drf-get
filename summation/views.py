from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from summation.serializers import SummationSerializers


@api_view(['GET'])
def summation(request):
    serializer = SummationSerializers(data=request.data)
    if serializer.is_valid():
        response = {"sum": serializer.data.get('a') + serializer.data.get('b')}
        return Response(response, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
