from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import User
from articles.serializers import (
    ArticleListSerializer,
    CommentListSerializer,
)


class Userserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"

    def create(self,validated_data):
        user=super().create(validated_data)
        password=user.password
        user.set_password(password)
        user.save()
        return user
    
    def update(self,validated_data):
        user=super().create(validated_data)
        password=user.password
        user.set_password(password)
        user.save()
        return user
    

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token
    

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=("username","email","fullname","nickname","date_of_birth",)

class UserArticleSerializer(serializers.ModelSerializer):
    article_set=ArticleListSerializer(many=True)
    class Meta:
        model=User
        fields=("article_set",)


class UserCommentSerializer(serializers.ModelSerializer):
    comment_set=CommentListSerializer(many=True)
    class Meta:
        model=User
        fields=("comment_set",)
