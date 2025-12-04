#!/usr/bin/env python
"""
Скрипт для загрузки данных из фронтенда в Django модели
"""
import os
import sys
import django
from datetime import datetime

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from website.models import (
    HeroSection, AboutSection, Partner, TeamMember, 
    Service, InsightCategory, Insight, ContactInfo
)

def load_hero_data():
    """Загрузка данных для Hero секции"""
    print("Загрузка Hero данных...")
    
    # Очистка существующих данных
    HeroSection.objects.all().delete()
    
    hero_data = {
        'title': 'Правовое сопровождение инвестиций',
        'subtitle': 'Комплексное юридическое сопровождение на всех этапах инвестиционного процесса',
        'description': 'Наша команда экспертов обеспечивает профессиональную поддержку инвестиционных проектов от структурирования до завершения сделок.',
        'cta_text': 'Подробнее',
        'cta_link': '#services',
        'is_active': True,
        'order': 1
    }
    
    HeroSection.objects.create(**hero_data)
    print("✓ Hero данные загружены")

def load_about_data():
    """Загрузка данных О нас"""
    print("Загрузка данных О нас...")
    
    # Очистка существующих данных
    AboutSection.objects.all().delete()
    
    about_data = {
        'title': 'О компании MBNAK',
        'description': 'Мы предоставляем комплексные консалтинговые услуги в области права, финансов и управления проектами. Наша команда экспертов с международным опытом помогает клиентам достигать поставленных целей.',
        'mission': 'Обеспечивать высококачественные консалтинговые услуги, способствующие успешному развитию бизнеса наших клиентов.',
        'vision': 'Стать ведущей консалтинговой компанией в регионе, известной своим профессионализмом и инновационными решениями.',
        'values': 'Профессионализм, Честность, Инновации, Клиентоориентированность, Результативность',
        'is_active': True
    }
    
    AboutSection.objects.create(**about_data)
    print("✓ Данные О нас загружены")

def load_services_data():
    """Загрузка услуг"""
    print("Загрузка услуг...")
    
    # Очистка существующих данных
    Service.objects.all().delete()
    
    services_data = [
        {
            'title': 'Правовое сопровождение инвестиций',
            'description': 'Комплексное юридическое сопровождение инвестиционных проектов на всех этапах',
            'short_description': 'Юридическое сопровождение инвестиций',
            'features': 'Структурирование инвестиционных сделок\nПодготовка и согласование документации\nПравовая экспертиза проектов\nСопровождение сделок M&A\nЗащита интересов инвесторов',
            'is_active': True,
            'is_featured': True,
            'order': 1
        },
        {
            'title': 'Корпоративное право',
            'description': 'Решение корпоративных споров, защита интеллектуальной собственности',
            'short_description': 'Корпоративное право и IP',
            'features': 'Разрешение корпоративных конфликтов\nЗащита прав акционеров\nРегистрация и защита IP\nКорпоративное управление\nРеорганизация бизнеса',
            'is_active': True,
            'is_featured': True,
            'order': 2
        },
        {
            'title': 'Финансово-кредитные правоотношения',
            'description': 'Юридическое сопровождение финансовых и кредитных операций',
            'short_description': 'Финансовое право',
            'features': 'Структурирование финансирования\nРабота с кредитными соглашениями\nСекьюритизация активов\nОблигационные займы\nБанковские споры',
            'is_active': True,
            'is_featured': False,
            'order': 3
        },
        {
            'title': 'Due Diligence',
            'description': 'Комплексная проверка объектов инвестирования и контрагентов',
            'short_description': 'Комплексная проверка',
            'features': 'Правовая проверка\nФинансовая проверка\nНалоговая проверка\nПроверка недвижимости\nАнализ рисков',
            'is_active': True,
            'is_featured': True,
            'order': 4
        },
        {
            'title': 'Кредитный брокер',
            'description': 'Поиск оптимальных условий финансирования для вашего бизнеса',
            'short_description': 'Кредитное посредничество',
            'features': 'Анализ потребностей в финансировании\nПодбор кредитных продуктов\nПереговоры с финансовыми институтами\nПодготовка документации\nСопровождение до получения средств',
            'is_active': True,
            'is_featured': False,
            'order': 5
        },
        {
            'title': 'ESG консалтинг',
            'description': 'Внедрение стандартов устойчивого развития и корпоративной ответственности',
            'short_description': 'ESG и устойчивое развитие',
            'features': 'ESG-стратегия и политики\nОценка ESG-рисков\nESG-отчетность\nУстойчивое финансирование\nСоответствие международным стандартам',
            'is_active': True,
            'is_featured': True,
            'order': 6
        },
        {
            'title': 'Коммуникации с государственными органами',
            'description': 'Взаимодействие с регуляторами и государственными структурами',
            'short_description': 'GR и взаимодействие с госорганами',
            'features': 'Получение разрешений и лицензий\nВзаимодействие с регуляторами\nПредставительство в госорганах\nУчастие в государственных закупках\nРазрешение административных споров',
            'is_active': True,
            'is_featured': False,
            'order': 7
        },
        {
            'title': 'Управление человеческим капиталом',
            'description': 'Стратегическое управление персоналом и развитие HR-процессов',
            'short_description': 'HR-консалтинг',
            'features': 'HR-стратегия\nПодбор топ-менеджмента\nСистемы мотивации\nТрудовое право\nКорпоративная культура',
            'is_active': True,
            'is_featured': False,
            'order': 8
        },
        {
            'title': 'Управление налоговыми обязательствами',
            'description': 'Оптимизация налоговой нагрузки и управление налоговыми рисками',
            'short_description': 'Налоговый консалтинг',
            'features': 'Налоговое планирование\nОптимизация налоговой структуры\nУправление налоговыми рисками\nНалоговые споры\nМеждународное налогообложение',
            'is_active': True,
            'is_featured': False,
            'order': 9
        },
        {
            'title': 'Управление инвестиционными проектами',
            'description': 'Профессиональное управление инвестиционными проектами от идеи до реализации',
            'short_description': 'Управление проектами',
            'features': 'Планирование проектов\nКонтроль бюджета и сроков\nУправление рисками\nКоординация подрядчиков\nОтчетность перед инвесторами',
            'is_active': True,
            'is_featured': False,
            'order': 10
        },
        {
            'title': 'Управление международными проектами',
            'description': 'Сопровождение международных проектов с учетом специфики разных юрисдикций',
            'short_description': 'Международные проекты',
            'features': 'Работа в разных юрисдикциях\nМежкультурные коммуникации\nМеждународные стандарты\nВалютные риски\nТрансграничные операции',
            'is_active': True,
            'is_featured': False,
            'order': 11
        }
    ]
    
    for service_data in services_data:
        Service.objects.create(**service_data)
    
    print(f"✓ Загружено {len(services_data)} услуг")

def load_team_data():
    """Загрузка команды"""
    print("Загрузка команды...")
    
    # Очистка существующих данных
    TeamMember.objects.all().delete()
    
    team_data = [
        {
            'name': 'Иван Петров',
            'position': 'Руководитель практики корпоративного права',
            'bio': '12+ лет опыта в корпоративном праве, специализация на M&A, интеллектуальной собственности и судебных спорах',
            'email': 'i.petrov@mbnak.com',
            'linkedin': 'https://linkedin.com/in/ivan-petrov',
            'is_active': True,
            'order': 1
        },
        {
            'name': 'Елена Соколова',
            'position': 'Партнер, практика инвестиций',
            'bio': 'Эксперт в структурировании инвестиционных сделок и международном финансировании',
            'email': 'e.sokolova@mbnak.com',
            'linkedin': 'https://linkedin.com/in/elena-sokolova',
            'is_active': True,
            'order': 2
        },
        {
            'name': 'Дмитрий Волков',
            'position': 'Руководитель направления ESG',
            'bio': 'Специалист по устойчивому развитию и корпоративной ответственности, опыт работы с международными стандартами',
            'email': 'd.volkov@mbnak.com',
            'linkedin': 'https://linkedin.com/in/dmitry-volkov',
            'is_active': True,
            'order': 3
        },
        {
            'name': 'Анна Михайлова',
            'position': 'Руководитель практики налогов',
            'bio': 'Специалист по налоговому планированию и оптимизации налоговых обязательств в международных структурах',
            'email': 'a.mikhailova@mbnak.com',
            'linkedin': 'https://linkedin.com/in/anna-mikhailova',
            'is_active': True,
            'order': 4
        }
    ]
    
    for member_data in team_data:
        TeamMember.objects.create(**member_data)
    
    print(f"✓ Загружено {len(team_data)} членов команды")

def load_partners_data():
    """Загрузка партнеров"""
    print("Загрузка партнеров...")
    
    # Очистка существующих данных
    Partner.objects.all().delete()
    
    partners_data = [
        {
            'name': 'Microsoft',
            'website': 'https://microsoft.com',
            'description': 'Стратегический технологический партнер',
            'is_active': True,
            'order': 1
        },
        {
            'name': 'Amazon Web Services',
            'website': 'https://aws.amazon.com',
            'description': 'Облачные решения и инфраструктура',
            'is_active': True,
            'order': 2
        },
        {
            'name': 'Google Cloud',
            'website': 'https://cloud.google.com',
            'description': 'Платформа для цифровой трансформации',
            'is_active': True,
            'order': 3
        },
        {
            'name': 'IBM',
            'website': 'https://ibm.com',
            'description': 'Корпоративные решения и консалтинг',
            'is_active': True,
            'order': 4
        },
        {
            'name': 'Oracle',
            'website': 'https://oracle.com',
            'description': 'Базы данных и корпоративные приложения',
            'is_active': True,
            'order': 5
        },
        {
            'name': 'SAP',
            'website': 'https://sap.com',
            'description': 'ERP системы и бизнес-приложения',
            'is_active': True,
            'order': 6
        }
    ]
    
    for partner_data in partners_data:
        Partner.objects.create(**partner_data)
    
    print(f"✓ Загружено {len(partners_data)} партнеров")

def load_insights_data():
    """Загрузка статей и категорий"""
    print("Загрузка статей...")
    
    # Очистка существующих данных
    InsightCategory.objects.all().delete()
    Insight.objects.all().delete()
    
    # Создание категорий
    categories_data = [
        {
            'name': 'ESG и устойчивое развитие',
            'slug': 'esg',
            'description': 'Статьи о факторах ESG и устойчивом развитии'
        },
        {
            'name': 'Слияния и поглощения',
            'slug': 'ma',
            'description': 'Материалы по M&A сделкам и due diligence'
        },
        {
            'name': 'Налоговое планирование',
            'slug': 'tax',
            'description': 'Налоговые вопросы и планирование'
        },
        {
            'name': 'Корпоративное управление',
            'slug': 'governance',
            'description': 'Вопросы корпоративного управления'
        },
        {
            'name': 'Интеллектуальная собственность',
            'slug': 'ip',
            'description': 'Защита интеллектуальной собственности'
        },
        {
            'name': 'Венчурное финансирование',
            'slug': 'venture',
            'description': 'Венчурные инвестиции и стартапы'
        }
    ]
    
    categories = {}
    for cat_data in categories_data:
        category = InsightCategory.objects.create(**cat_data)
        categories[cat_data['slug']] = category
    
    # Создание статей
    insights_data = [
        {
            'title': 'ESG-факторы: как влияют на стоимость капитала в регионе',
            'slug': 'esg-factors-capital-cost',
            'excerpt': 'Анализ влияния ESG-критериев на оценку инвестиционной привлекательности компаний в странах Центральной Азии',
            'content': '''ESG-факторы становятся ключевым элементом инвестиционных решений. В регионе Центральной Азии компании, внедряющие ESG-практики, получают доступ к более дешевому капиталу и демонстрируют устойчивый рост.

Основные направления влияния ESG на стоимость капитала:
- Снижение рисков и повышение инвестиционной привлекательности
- Доступ к зеленому финансированию
- Улучшение операционной эффективности
- Повышение репутации и лояльности клиентов''',
            'category': categories['esg'],
            'author': 'Дмитрий Волков',
            'is_published': True,
            'is_featured': True
        },
        {
            'title': 'Due Diligence 2.0: что реально проверяют инвесторы',
            'slug': 'due-diligence-2024',
            'excerpt': 'Современные подходы к комплексной проверке объектов инвестирования: от финансов до киберрисков',
            'content': '''Процедура Due Diligence кардинально изменилась. Современные инвесторы применяют комплексный подход, включающий:

- Цифровую трансформацию и IT-инфраструктуру
- Кибербезопасность и защиту данных  
- ESG-факторы и устойчивое развитие
- Репутационные риски и медиа-анализ
- Технологические активы и инновационный потенциал''',
            'category': categories['ma'],
            'author': 'Елена Соколова',
            'is_published': True,
            'is_featured': True
        },
        {
            'title': 'Управление налоговыми рисками при международной экспансии',
            'slug': 'tax-risk-management',
            'excerpt': 'Ключевые аспекты налогового планирования при выходе на новые рынки и организации трансграничных операций',
            'content': '''Международная экспансия создает сложные налоговые вызовы. Эффективное управление налоговыми рисками включает:

- Предварительное планирование налоговой структуры
- Соблюдение требований трансфертного ценообразования
- Управление рисками постоянного представительства
- Оптимизация НДС при трансграничных операциях''',
            'category': categories['tax'],
            'author': 'Анна Михайлова',
            'is_published': True,
            'is_featured': False
        },
        {
            'title': 'Тренды корпоративного управления 2025',
            'slug': 'corporate-governance-trends-2025',
            'excerpt': 'Как меняются подходы к корпоративному управлению в условиях цифровизации и глобальных вызовов',
            'content': '''Корпоративное управление эволюционирует под влиянием технологий и ESG-требований:

- Цифровизация процессов советов директоров
- Интеграция ESG в корпоративную стратегию
- Разнообразие и инклюзивность в управлении
- Стейкхолдер-капитализм и долгосрочное создание стоимости''',
            'category': categories['governance'],
            'author': 'Иван Петров',
            'is_published': True,
            'is_featured': False
        },
        {
            'title': 'Защита интеллектуальной собственности в цифровую эпоху',
            'slug': 'ip-protection-digital-age',
            'excerpt': 'Новые вызовы и инструменты защиты IP в условиях развития AI и цифровых технологий',
            'content': '''Цифровая трансформация создает новые вызовы для защиты IP:

- Авторство произведений, созданных ИИ
- Защита больших данных как интеллектуальной собственности
- Блокчейн и NFT в системе IP-прав
- Международное правоприменение в цифровой среде''',
            'category': categories['ip'],
            'author': 'Иван Петров',
            'is_published': True,
            'is_featured': False
        },
        {
            'title': 'Альтернативные источники финансирования для стартапов',
            'slug': 'alternative-startup-financing',
            'excerpt': 'Обзор современных инструментов привлечения капитала: от венчура до краудфандинга',
            'content': '''Экосистема финансирования стартапов расширилась:

- Краудфандинг и equity crowdfunding
- Revenue-based financing (RBF)
- Токенизация и криптофинансирование  
- Корпоративное венчурное финансирование
- Государственные и международные программы поддержки''',
            'category': categories['venture'],
            'author': 'Елена Соколова',
            'is_published': True,
            'is_featured': False
        }
    ]
    
    for insight_data in insights_data:
        Insight.objects.create(**insight_data)
    
    print(f"✓ Загружено {len(categories_data)} категорий и {len(insights_data)} статей")

def load_contact_data():
    """Загрузка контактной информации"""
    print("Загрузка контактной информации...")
    
    # Очистка существующих данных
    ContactInfo.objects.all().delete()
    
    contact_data = {
        'company_name': 'MBNAK Consulting',
        'address': 'г. Алматы, ул. Достык, 123, офис 456',
        'phone': '+7 (727) 123-45-67',
        'email': 'info@mbnak.com',
        'website': 'https://mbnak.com',
        'working_hours': 'Пн-Пт: 9:00-18:00\nСб-Вс: выходной',
        'linkedin': 'https://linkedin.com/company/mbnak',
        'is_active': True
    }
    
    ContactInfo.objects.create(**contact_data)
    print("✓ Контактная информация загружена")

def main():
    """Основная функция загрузки данных"""
    print("Начинаем загрузку данных из фронтенда в Django...")
    print("=" * 50)
    
    try:
        load_hero_data()
        load_about_data()
        load_services_data()
        load_team_data()
        load_partners_data()
        load_insights_data()
        load_contact_data()
        
        print("=" * 50)
        print("✅ Все данные успешно загружены!")
        print("\nТеперь вы можете:")
        print("1. Запустить Django сервер: python manage.py runserver")
        print("2. Открыть админку: http://127.0.0.1:8000/admin/")
        print("3. Посмотреть API: http://127.0.0.1:8000/api/website-data/")
        
    except Exception as e:
        print(f"❌ Ошибка при загрузке данных: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
