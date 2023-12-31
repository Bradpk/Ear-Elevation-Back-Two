from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from rest_framework import routers
from .views import *
#------------------------------------------------------------------------------------------------------------------------------
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'user-logs', UserLogViewSet)
#------------------------------------------------------------------------------------------------------------------------------
urlpatterns = [
    path('', include(router.urls)),
    path('user-log/<int:user_id>/', FilteredUserLogListView.as_view(), name='filtered_user_logs'),
    path('user/signup/', UserCreate.as_view(), name="create_user"),
    path('huh/<int:pk>/', UserDetail.as_view(), name="get_user_details"),
    path('user/login/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]