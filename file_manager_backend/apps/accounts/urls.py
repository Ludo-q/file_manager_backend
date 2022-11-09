from django.urls import path
from knox import views as knox_views
from file_manager_backend.apps.accounts.views import LoginView

urlpatterns = [
    path(r'login/', LoginView.as_view(), name='knox_login')
]
