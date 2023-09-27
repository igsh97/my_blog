from rest_framework import serializers

from .models import Article,Comment

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=("content",)


class CommentSerializer(serializers.ModelSerializer):
    user=serializers.SerializerMethodField()
    def get_user(self,obj):
        return obj.user.username
    class Meta:
        model=Comment
        exclude=("article",)

class ArticleSerializer(serializers.ModelSerializer):
    user=serializers.SerializerMethodField()
    comment_set=CommentSerializer(many=True)
    def get_user(self,obj):
        return obj.author.username
    class Meta:
        model=Article
        fields='__all__'


class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Article
        fields=("title","content")


class ArticleListSerializer(serializers.ModelSerializer):
    author=serializers.SerializerMethodField()
    comments_count=serializers.SerializerMethodField()
    def get_author(self,obj):
        return obj.author.username
    def get_comments_count(self,obj):
        return obj.comment_set.count()
    class Meta:
        model=Article
        fields=('pk','title','updated_at','author','comments_count')


class CommentListSerializer(serializers.ModelSerializer):
    user=serializers.SerializerMethodField()
    article=serializers.SerializerMethodField()
    def get_user(self,obj):
        return obj.user.username
    def get_article(self,obj):
        return obj.article.title
    class Meta:
        model=Comment
        fields=('user','article','content',)