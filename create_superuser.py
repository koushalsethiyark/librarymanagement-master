import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'librarymanagement.settings')
django.setup()

from django.contrib.auth.models import User

username = 'rk'
password = '123'

user, created = User.objects.get_or_create(username=username, defaults={'is_superuser': True, 'is_staff': True})
if created:
    user.set_password(password)
    user.save()
    print(f"Superuser '{username}' created successfully.")
else:
    if not user.is_superuser:
        user.is_superuser = True
        user.is_staff = True
        user.set_password(password)
        user.save()
        print(f"User '{username}' updated to superuser.")
    else:
        print(f"Superuser '{username}' already exists.")
