from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Activity
from .serializers import ActivitySerializer
from rest_framework import filters

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    odering_fields = ['date', 'duration', 'calories_burned']

def get_queryset(self):
    return self.queryset.filter(user = self.request.user)

def perform_create(self, serializer):
    serializer.save(user=self.request.user)


from rest_framework import viewsets 
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Activity
from .serializers import ActivitySerializer
from django.utils.dateparse import parse_date


class ActivityHistoryViewSet(viewsets.ViewSet):
    
    permission_classes = [IsAuthenticated]

    def list (self, request):
        user = request.user
        activities = Activity.objects.filter(user=user)
        
                        
        activity_type = request.query_params.get('activity_type')
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        if activity_type:
            activities = activities.filter(activity_type=activity_type)
        if start_date:
            activities = activities.filter(date__gte=parse_date(start_date))
        if end_date:
            activities = activities.filter(date__lte=parse_date(end_date))

        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data)
    



from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Sum
from .models import Activity
from django.utils.dateparse import parse_date



class ActivityMetricsViewSet(viewsets.ViewSet):

    permission_classes = [IsAuthenticated]

    def list(self, request):
        user = request.user
        activities = Activity.objects.filter(user=user)

        

        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        if start_date:
            activities = activities.filter(date__gte=parse_date(start_date)) 
        
        if end_date:
            activities = activities.filter(date__lte=parse_date(end_date))


        metrics = activities.aaggregate(
            total_duration=Sum('duration'),
            total_distance=Sum('distance'),
            total_calories=Sum('calories_burned')
        )    

        metrics['total_duration'] = metrics['total_duration'] or 0
        metrics['total_distance'] = metrics['total_distance'] or 0.0
        metrics['total_calories'] = metrics['total_calories'] or 0.0

        return Response(metrics)






   
from rest_framework import generics
from .models import Activity  
from .serializers import ActivitySerializer  

class ActivityListView(generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class ActivityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
 