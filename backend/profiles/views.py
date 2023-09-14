from rest_framework.generics import RetrieveUpdateAPIView

from .models import Profile
from .serializers import ProfileSerializer


class ProfileView(RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
