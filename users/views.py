from rest_framework.views import APIView
from rest_framework import status,permissions
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .serializers import (
    Userserializer,
    CustomTokenObtainPairSerializer,
    UserProfileSerializer,
    UserArticleSerializer,
    UserCommentSerializer,
)
from .models import User

# Create your views here.
class UserView(APIView):
    def post(self,request):
        serializer=Userserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"가입완료!"},status=status.HTTP_201_CREATED)
        else:
            return Response({"message":f"${serializer.errors}"},status=status.HTTP_400_BAD_REQUEST)
        

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class=CustomTokenObtainPairSerializer


class ProfileView(APIView):
    def get(self,request,user_id):
        user=get_object_or_404(User,id=user_id)
        serializer=UserProfileSerializer(user)
        return Response(serializer.data,status=status.HTTP_200_OK)
    

class UserArticleView(APIView):
    def get(self,request,user_id):
        user=get_object_or_404(User,id=user_id)
        serializer=UserArticleSerializer(user)
        return Response(serializer.data,status=status.HTTP_200_OK)
    

class UserCommentView(APIView):
    def get(self,request,user_id):
        user=get_object_or_404(User,id=user_id)
        serializer=UserCommentSerializer(user)
        return Response(serializer.data,status=status.HTTP_200_OK)