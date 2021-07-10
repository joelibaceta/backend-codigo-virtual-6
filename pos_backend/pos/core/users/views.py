from core.users.serializers import CustomObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class CustomObtainPairView(TokenObtainPairView):
    serializer_class = CustomObtainPairSerializer