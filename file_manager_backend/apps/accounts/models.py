from django.db import models
from django.contrib.auth.models import User


class UserFileManager(User):

    class Meta:
        default_permissions = ('add', 'delete')
        permissions = [
            ('can_add_new_file', 'The user can add new file')
        ]
