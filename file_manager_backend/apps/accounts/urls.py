from django.urls import path
from knox import views as knox_views
from .views import LoginView, UserFileManagerListView, PermissionListView

urlpatterns = [
    path(r'', UserFileManagerListView.as_view(), name='user_list'),
    path(r'permissions/', PermissionListView.as_view(), name='permission_list'),
    path(r'login/', LoginView.as_view(), name='knox_login'),
    path(r'logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path(r'logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
]


app_name = 'accounts'
