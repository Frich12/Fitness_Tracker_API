from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ActivityViewSet, ActivityHistoryViewSet , ActivityMetricsViewSet

router = DefaultRouter()
router.register(r'activities', ActivityViewSet, basename='activity')
router.register(r'activity-history', ActivityHistoryViewSet, basename='activity-history')
router.register(r'activity-metrics', ActivityMetricsViewSet, basename='activity-metrics')

urlpatterns = [
    path('api/', include(router.urls)),
]

from django.urls import path
from .views import ActivityViewSet  

urlpatterns = [
    path('', ActivityViewSet.as_view({'get': 'list', 'post': 'create'}), name='activity-list'),  
    path('<int:pk>/', ActivityViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='activity-detail'),  
]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.ActivityListView.as_view(), name='activity-list'),  
    path('<int:pk>/', views.ActivityDetailView.as_view(), name='activity-detail'),  
]


