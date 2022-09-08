from django.contrib import admin
from django.urls import path, include
from .routers import router
import django_cas_ng.views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', django_cas_ng.views.LoginView.as_view(), name='cas_ng_login'),
    path('api/logout/', django_cas_ng.views.LogoutView.as_view(), name='cas_ng_logout'),
    # path('logout/', views.MyLogoutView.as_view(), name='cas_ng_logout'),
    path('api/', include(router.urls), name='api'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
