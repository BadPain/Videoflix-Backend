from django.urls import path, re_path
from .views import RegisterView, LoginView, LogoutView, ActivateView, RequestPasswordResetView, PasswordResetConfirmView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('activate/<uidb64>/<token>/', ActivateView.as_view(), name='activate'),
    path('password_reset/', RequestPasswordResetView.as_view(), name='password_reset'),
    re_path(r'^password_confirm/(?P<uidb64>[^/]+)/(?P<token>[^/]+)/?/?$', PasswordResetConfirmView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]