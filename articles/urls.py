from django.urls import path

from . import views

urlpatterns = [
    path('',views.ArticleView.as_view(),name='article_view'),
    path('user/<int:user_id>/',views.AritcleUserListView.as_view(),name='article_user_view'),
    path('<int:article_id>/',views.AritcleDetailView.as_view(),name='article_user_detail_view'),
    path('<int:article_id>/comment/',views.CommentView.as_view(),name='comment_view'),
    path('<int:article_id>/comment/<int:comment_id>/',views.CommentDetailView.as_view(),name='comment_detail_view'),
]