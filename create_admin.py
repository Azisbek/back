#!/usr/bin/env python
"""
Скрипт для создания суперпользователя Django
"""
import os
import django

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from django.contrib.auth.models import User

def create_superuser():
    """Создание суперпользователя"""
    username = 'admin'
    email = 'admin@mbnak.com'
    password = 'admin123'
    
    if User.objects.filter(username=username).exists():
        print(f"Пользователь '{username}' уже существует!")
        user = User.objects.get(username=username)
        print(f"Email: {user.email}")
        print(f"Логин: {username}")
        print(f"Пароль: admin123")
    else:
        User.objects.create_superuser(username=username, email=email, password=password)
        print(f"✅ Суперпользователь создан!")
        print(f"Логин: {username}")
        print(f"Email: {email}")
        print(f"Пароль: {password}")
    
    print(f"\n🔗 Админка доступна по адресу: http://localhost:8000/admin/")

if __name__ == '__main__':
    create_superuser()




