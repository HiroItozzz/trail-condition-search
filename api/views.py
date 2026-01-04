from rest_framework import generics
from trail_status.models.condition import TrailCondition
from trail_status.models.source import DataSource
from api.permissions import IsAdminUserOrReadOnly
from api.serializers import TrailConditionSerializer

class ListView(generics.ListCreateAPIView):
    queryset = TrailCondition.objects.all().order_by("-updated_at")
    serializer_class = TrailConditionSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class DetailView(generics.RetrieveAPIView):
    queryset = TrailCondition.objects.all()
    serializer_class = TrailConditionSerializer
    permission_classes = [IsAdminUserOrReadOnly]