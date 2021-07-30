from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self,request,format=None):
        """Return A list of APIView feature"""
        an_apiview=[
        'Uses HTTP method as function(get,post,patch,put,delete)',
        'Is similar to traditional Django View',
        'Gives you the most control over your application Logic',
        'Is mapped manually to URLs'
        ]
        return Response({'message':'hello','an_apiview':an_apiview})
