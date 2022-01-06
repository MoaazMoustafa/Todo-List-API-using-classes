from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from tasks.models import Task
from .serializers import TaskSerializer
from django.shortcuts import get_object_or_404

# class home(APIView):
#     def get(self, request):
#         tasks = Task.objects.all().order_by('-time')
#         ser_tasks = TaskSerializer(tasks, many=True)
#         return Response(data=ser_tasks.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         task = TaskSerializer(data=request.data)
#         if task.is_valid():
#             task.save()
#             return Response(data=task.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(data=task.errors, status=status.HTTP_400_BAD_REQUEST)


# class detail(APIView):
#     def get(self, request, id):
#         task = get_object_or_404(Task, id=id)
#         ser_task = TaskSerializer(task)
#         return Response(data=ser_task.data, status=status.HTTP_200_OK)

#     def patch(self, request, id):
#         task = get_object_or_404(Task, id=id)
#         ser_task = TaskSerializer(instance=task, data=request.data)
#         if ser_task.is_valid():
#             ser_task.save()
#             return Response(data=ser_task.data, status=status.HTTP_202_ACCEPTED)
#         else:
#             return Response(data=ser_task.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, id):
#         task = get_object_or_404(Task, id=id)
#         task.delete()
#         return Response(data={'message': 'deleted'}, status=status.HTTP_202_ACCEPTED)


# ------------------------------ Generic Views -----------------------------------------


# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


# class TaskListCreateView(ListCreateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer


# class TaskDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer


# -------------------------------------Viewsets------------------------

from rest_framework import viewsets


class TaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
