import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shopproject.settings') 
django.setup()

def create_superuser():
    User = get_user_model()
    username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
    email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
    password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

    if not username or not email or not password:
        return  

    if not User.objects.filter(username=username).exists():
        print(f"Создание суперпользователя {username}...")
        User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        print("Суперпользователь успешно создан! :)")
    else:
        print("Суперпользователь уже существует или возникла ошибка :(")

if __name__ == "__main__":
    create_superuser()

