from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated




from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions



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


class HelloViewSet(viewsets.ViewSet):
    """"Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self,request):
        """Return a hello Message"""
        a_viewset = [
        'User Actions (list,create.retrieve.update,partial update)',
        'Automatically maps to URLs using Routers',
        'Provides more functionaly using less code'
        ]

        return Response ({'message':'Hello','a_viewsets':a_viewset})

    def create(self,request):
        """Create a Hello Message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request,pk=None):
        """Handle getting an object by its ID"""
        return Response({'Http_Method': 'Get'})


    def update(self, request,pk=None):
        """Handle updating an object by its ID"""
        return Response({'Http_Method': 'PUT'})


    def partial_update(self, request,pk=None):
        """Handle update part of an object by its ID"""
        return Response({'Http_Method': 'PATCH'})


    def destroy(self, request,pk=None):
        """Handle destroy an object by its ID"""
        return Response({'Http_Method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profile"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email')


class UserLoginApiView(ObtainAuthToken):
    """"Handle creating user Authentication Tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles  Creating, reading and updating profile field items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatus,IsAuthenticated)

    def perform_create(self, serializer):
        """Sets the user_profile to the logged in User"""
        serializer.save(user_profile=self.request.user)
