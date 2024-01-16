from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from django.http import JsonResponse
from .models import *
from .serializers import MovieSerializer


class MovieList(APIView):
    
    def get(self, request):
        try: 
            movies= Movie.objects.all()
        except:
            context={'Error': 'No movies were found'}
            return Response(context, status= status.HTTP_404_NOT_FOUND)
            
        serializer = MovieSerializer(movies, many= True)
        return Response (serializer.data)
    
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
        
class MovieDetails(APIView):
    
    def get(self, request, pk):
        try: 
            movie = Movie.objects.get(id=pk)
        except:
            context={'Error': 'No movie was found'}
            return Response(context, status= status.HTTP_404_NOT_FOUND)
        serializer= MovieSerializer(movie)
        return Response(serializer.data)
    
    def put(self, request, pk):
        movie=Movie.objects.get(id=pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        movie = Movie.objects.get (id=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

