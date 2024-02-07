from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from django.http import JsonResponse
from .models import *
from .serializers import WatchListSerializer, StreamPlatfromSerializer


class WatchList(APIView):
    
    def get(self, request):
        try: 
            WatchLists= WatchList.objects.all()
        except:
            context={'Error': 'No WatchLists were found'}
            return Response(context, status= status.HTTP_404_NOT_FOUND)
            
        serializer = WatchListSerializer(WatchLists, many= True)
        return Response (serializer.data)
    
    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
        
class WatchList_Details(APIView):
    
    def get(self, request, pk):
        try: 
            WatchList = WatchList.objects.get(id=pk)
        except:
            context={'Error': 'No WatchList was found'}
            return Response(context, status= status.HTTP_404_NOT_FOUND)
        
        serializer= WatchListSerializer(WatchList)
        return Response(serializer.data)
    
    def put(self, request, pk):
        WatchList=WatchList.objects.get(id=pk)
        serializer = WatchListSerializer(WatchList, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        WatchList = WatchList.objects.get (id=pk)
        WatchList.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StreamPlatformList(APIView):
    def get(self,request):
        try:
            platform_list = StreamPlatform.objects.all()
        except:
            context = {"Error":"No platforms were found in the database"}
            return Response(context, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StreamPlatfromSerializer(platform_list, many=True)
        return Response(serializer.data)
        
    
    def post(self, request):
        serializer = StreamPlatfromSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class StreamPlatform_details(APIView):
    def get(self,request, pk):
        try:
            platform = StreamPlatform.objects.get(id=pk)
        except: 
            context={'Error':'No such platform'}
            return Response(context, status= status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatfromSerializer(platform)
        return Response(serializer.data)