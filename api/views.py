from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer

from .models import Task

@api_view(['GET'])
def apiOverView(request):
    api_urls = {
        'List':'/todo-list/',
		'Detail View':'/todo-detail/<str:pk>/',
		'Create':'/todo-create/',
		'Update':'/todo-update/<str:pk>/',
		'Delete':'/todo-delete/<str:pk>/',
    }

    return Response(api_urls)

@api_view(['GET'])
def todoList(request):
    todos = Task.objects.all().order_by('-id')
    serializer = TaskSerializer(todos, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def todoDetail(request, pk):
	todos = Task.objects.get(id=pk)
	serializer = TaskSerializer(todos, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def todoCreate(request):
	serializer = TaskSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def todoUpdate(request, pk):
	task = Task.objects.get(id=pk)
	serializer = TaskSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def todoDelete(request, pk):
	todo = Task.objects.get(id=pk)
	todo.delete()

	return Response('Item succsesfully delete!')
        
        
    