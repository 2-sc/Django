from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics

from .models import Planner
from .serializers import TodoSerializer


# Create your view here.

class TodoAPIView(APIView):
    def get(self, request):
        todos = Planner.objects.all()
        serializers = TodoSerializer(todos, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


class TodoCreateAPIView(APIView):
    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoDetailAPIView(APIView):
    def put(self, request, pk):
        todo = get_object_or_404(Planner, id=pk)
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        todo = get_object_or_404(Planner, id=pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
