from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('file_manager_backend.apps.accounts.urls', namespace='accounts')),
]

