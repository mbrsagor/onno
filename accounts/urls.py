from django.urls import path

from .views import (
    ChangePasswordView,
    CreateUserView,
    UpdateUserView,
    DetailUserView,
    UserLoginView
)

urlpatterns = [
    path('login/', UserLoginView.as_view(), name="login"),
    path('register/', CreateUserView.as_view(), name="register"),
    path('<int:pk>/update-account/', UpdateUserView.as_view(), name="update-account"),
    path('<int:pk>/account/', DetailUserView.as_view(), name="detail-account"),
    path('password-change/<int:pk>/', ChangePasswordView.as_view(), name="password_change"),
]
