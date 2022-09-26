from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import LoginSerializer, ProfileSerializer, RegisterSerializer
from .models import User


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        seiralizer = self.get_serializer(data=request.data)
        seiralizer.is_valid(raise_exception=True)
        token = seiralizer.validated_data

        return Response({'token': token.key}, status=status.HTTP_200_OK)


class UserProfileView(APIView):
    def get(self, request):
        user_profile = User.objects.get(email=self.request.user)
        serializer = ProfileSerializer(user_profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
