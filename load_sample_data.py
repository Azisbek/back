#!/usr/bin/env python
"""
Скрипт для загрузки примеров данных в базу данных
Запустите: python manage.py shell < load_sample_data.py
"""

import os
import django

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from website.models import *

def load_sample_data():
    print("🔄 Загрузка примеров данных...")
    
    # Hero Section
    hero, created = HeroSection.objects.get_or_create(
        title="Добро пожаловать в нашу компанию",
        defaults={
            'subtitle': 'Мы предоставляем лучшие решения для вашего бизнеса',
            'description': 'Наша команда профессионалов готова помочь вам достичь новых высот в бизнесе.',
            'cta_text': 'Узнать больше',
            'cta_link': '#about',
            'is_active': True,
            'order': 1
        }
    )
    if created:
        print("✅ Hero секция создана")
    
    # About Section
    about, created = AboutSection.objects.get_or_create(
        title="О нашей компании",
        defaults={
            'description': 'Мы — инновационная компания, которая помогает бизнесу расти и развиваться в цифровую эпоху.',
            'mission': 'Наша миссия — предоставлять качественные решения, которые помогают нашим клиентам достигать успеха.',
            'vision': 'Мы стремимся стать лидером в области цифровых решений для бизнеса.',
            'values': 'Качество, Инновации, Клиентоориентированность, Профессионализм',
            'is_active': True
        }
    )
    if created:
        print("✅ Секция 'О нас' создана")
    
    # Partners
    partners_data = [
        {'name': 'Google', 'description': 'Технологический партнер'},
        {'name': 'Microsoft', 'description': 'Облачные решения'},
        {'name': 'Amazon', 'description': 'AWS партнер'},
    ]
    
    for i, partner_data in enumerate(partners_data):
        partner, created = Partner.objects.get_or_create(
            name=partner_data['name'],
            defaults={
                'description': partner_data['description'],
                'is_active': True,
                'order': i + 1
            }
        )
        if created:
            print(f"✅ Партнер {partner_data['name']} создан")
    
    # Team Members
    team_data = [
        {
            'name': 'Иван Иванов',
            'position': 'CEO',
            'bio': 'Опытный руководитель с 15-летним стажем в IT-индустрии.'
        },
        {
            'name': 'Мария Петрова',
            'position': 'CTO',
            'bio': 'Технический директор, эксперт в области разработки ПО.'
        },
        {
            'name': 'Алексей Сидоров',
            'position': 'Lead Developer',
            'bio': 'Ведущий разработчик с экспертизой в современных технологиях.'
        }
    ]
    
    for i, member_data in enumerate(team_data):
        member, created = TeamMember.objects.get_or_create(
            name=member_data['name'],
            defaults={
                'position': member_data['position'],
                'bio': member_data['bio'],
                'is_active': True,
                'order': i + 1
            }
        )
        if created:
            print(f"✅ Член команды {member_data['name']} создан")
    
    # Services
    services_data = [
        {
            'title': 'Веб-разработка',
            'description': 'Создание современных веб-приложений и сайтов',
            'short_description': 'Разработка сайтов и веб-приложений',
            'features': 'Адаптивный дизайн\nSEO-оптимизация\nБыстрая загрузка\nБезопасность',
            'price': 50000,
            'is_featured': True
        },
        {
            'title': 'Мобильная разработка',
            'description': 'Разработка мобильных приложений для iOS и Android',
            'short_description': 'Мобильные приложения',
            'features': 'iOS и Android\nНативная производительность\nИнтуитивный интерфейс',
            'price': 80000,
            'is_featured': True
        },
        {
            'title': 'Консультации',
            'description': 'IT-консультации и аудит существующих решений',
            'short_description': 'Экспертные консультации',
            'features': 'Анализ архитектуры\nОптимизация процессов\nРекомендации по улучшению',
            'price': 15000
        }
    ]
    
    for i, service_data in enumerate(services_data):
        service, created = Service.objects.get_or_create(
            title=service_data['title'],
            defaults={
                'description': service_data['description'],
                'short_description': service_data['short_description'],
                'features': service_data['features'],
                'price': service_data['price'],
                'is_featured': service_data.get('is_featured', False),
                'is_active': True,
                'order': i + 1
            }
        )
        if created:
            print(f"✅ Услуга {service_data['title']} создана")
    
    # Insight Categories
    categories_data = [
        {'name': 'Технологии', 'slug': 'tech'},
        {'name': 'Бизнес', 'slug': 'business'},
        {'name': 'Дизайн', 'slug': 'design'}
    ]
    
    for cat_data in categories_data:
        category, created = InsightCategory.objects.get_or_create(
            slug=cat_data['slug'],
            defaults={'name': cat_data['name']}
        )
        if created:
            print(f"✅ Категория {cat_data['name']} создана")
    
    # Insights
    tech_category = InsightCategory.objects.get(slug='tech')
    business_category = InsightCategory.objects.get(slug='business')
    
    insights_data = [
        {
            'title': 'Будущее веб-разработки в 2024',
            'slug': 'future-web-development-2024',
            'excerpt': 'Обзор главных трендов и технологий в веб-разработке',
            'content': 'Подробная статья о том, как развивается веб-разработка...',
            'category': tech_category,
            'author': 'Алексей Сидоров',
            'is_featured': True
        },
        {
            'title': 'Как цифровизация меняет бизнес',
            'slug': 'digital-transformation-business',
            'excerpt': 'Влияние цифровых технологий на современный бизнес',
            'content': 'Анализ того, как цифровая трансформация влияет на бизнес-процессы...',
            'category': business_category,
            'author': 'Мария Петрова',
            'is_featured': True
        }
    ]
    
    for insight_data in insights_data:
        insight, created = Insight.objects.get_or_create(
            slug=insight_data['slug'],
            defaults=insight_data
        )
        if created:
            print(f"✅ Статья {insight_data['title']} создана")
    
    # Contact Info
    contact, created = ContactInfo.objects.get_or_create(
        company_name="Наша IT Компания",
        defaults={
            'address': 'г. Москва, ул. Примерная, д. 123, офис 456',
            'phone': '+7 (495) 123-45-67',
            'email': 'info@ourcompany.ru',
            'website': 'https://ourcompany.ru',
            'working_hours': 'Пн-Пт: 9:00-18:00\nСб-Вс: выходные',
            'is_active': True
        }
    )
    if created:
        print("✅ Контактная информация создана")
    
    print("🎉 Загрузка примеров данных завершена!")
    print("\n📋 Что было создано:")
    print(f"- Hero секций: {HeroSection.objects.count()}")
    print(f"- Секций 'О нас': {AboutSection.objects.count()}")
    print(f"- Партнеров: {Partner.objects.count()}")
    print(f"- Членов команды: {TeamMember.objects.count()}")
    print(f"- Услуг: {Service.objects.count()}")
    print(f"- Категорий статей: {InsightCategory.objects.count()}")
    print(f"- Статей: {Insight.objects.count()}")
    print(f"- Контактной информации: {ContactInfo.objects.count()}")

if __name__ == "__main__":
    load_sample_data()
