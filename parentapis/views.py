from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from authentication.permissions import IsParent
from authentication.models import CustomUser
from .models import NotAllowedSearches
from .serializers import NotAllowedSearchesSerializer
from django.shortcuts import get_object_or_404


# Create your views here.
class NotAllowedSearchAPIView(APIView):
    permission_classes = [IsAuthenticated, IsParent]
    def get(self,request,pk):
        try:
            child = get_object_or_404(CustomUser, id=pk)
            searches = NotAllowedSearches.objects.filter(user=child)
            if not searches.exists():
                return Response({"message":"No Search Found"}, status=status.HTTP_200_OK)
            serializer = NotAllowedSearchesSerializer(searches, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": "An error occurred while processing your request."},status=status.HTTP_500_INTERNAL_SERVER_ERROR)