from django.urls import path
# from .views import home, detail
# urlpatterns = [
#     path('tasks', home.as_view(), name='home'),
#     path('task/<int:id>', detail.as_view(), name='detail'),
# ]
# from .views import TaskDetailView, TaskListCreateView
# urlpatterns = [
#     path('tasks', TaskListCreateView.as_view(), name='home'),
#     path('task/<int:pk>', TaskDetailView.as_view(), name='detail')
# ]
from rest_framework.routers import DefaultRouter

from .views import TaskViewset
router = DefaultRouter()
router.register('tasks', TaskViewset, basename='tasks')

urlpatterns = router.urls
