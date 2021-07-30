from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """Return A list of APIView feature"""
        an_apiview=[
        'Uses HTTP method as function(get,post,patch,put,delete)',
        'Is similar to traditional Django View',
        'Gives you the most control over your application Logic',
        'Is mapped manually to URLs'
        ]
        return Response({'message':'hello','an_apiview':an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})

        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def put(self,request,pk=None):
        """Handle updating objects"""
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        """Handlesa partial update of the object"""
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})
