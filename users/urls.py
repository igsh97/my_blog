from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView,
)
from . import views

urlpatterns = [
    path('signup/',views.UserView.as_view(),name='user_view'),
    path('api/token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/logout/',TokenBlacklistView.as_view(),name='token_blacklist'),
    path('<int:user_id>/',views.ProfileView.as_view(),name='Profile_view'),
    path('<int:user_id>/articles/',views.UserArticleView.as_view(),name='user_article_view'),
    path('<int:user_id>/comments/',views.UserCommentView.as_view(),name='user_comment_view'),
]