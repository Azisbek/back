# Развертывание Django приложения на Vercel

## Подготовка к развертыванию

### 1. Установка Vercel CLI
```bash
npm i -g vercel
```

### 2. Вход в аккаунт Vercel
```bash
vercel login
```

## Настройка переменных окружения

В панели управления Vercel (или через CLI) добавьте следующие переменные окружения:

### Обязательные переменные:
- `SECRET_KEY` - секретный ключ Django (сгенерируйте новый для продакшена)
- `DEBUG` - установите в `False`
- `DATABASE_URL` - URL подключения к PostgreSQL базе данных

### Опциональные переменные:
- `ALLOWED_HOSTS` - домены, которые могут обращаться к приложению
- `CORS_ALLOWED_ORIGINS` - домены для CORS (если используете фронтенд)

### Пример настройки через CLI:
```bash
vercel env add SECRET_KEY
vercel env add DEBUG
vercel env add DATABASE_URL
```

## База данных

Vercel не предоставляет встроенную базу данных PostgreSQL. Рекомендуется использовать:

1. **Vercel Postgres** (рекомендуется)
   - Создайте базу данных в панели Vercel
   - Скопируйте DATABASE_URL из настроек

2. **Внешние провайдеры:**
   - Railway
   - Supabase
   - ElephantSQL
   - Amazon RDS

## Развертывание

### Автоматическое развертывание (рекомендуется):
1. Подключите репозиторий GitHub к Vercel
2. Vercel автоматически развернет приложение при каждом push

### Ручное развертывание:
```bash
vercel --prod
```

## Миграции базы данных

После первого развертывания выполните миграции:

```bash
# Через Vercel CLI
vercel env pull .env.local
python manage.py migrate

# Или создайте суперпользователя
python manage.py createsuperuser
```

## Статические файлы

Статические файлы обрабатываются автоматически через Django's collectstatic.
Vercel автоматически обнаружит и соберет статические файлы при развертывании.

## Проверка развертывания

После развертывания проверьте:
1. Главная страница API: `https://your-app.vercel.app/api/`
2. Админка: `https://your-app.vercel.app/admin/`
3. Swagger документация: `https://your-app.vercel.app/api/docs/`

## Возможные проблемы

### 1. Ошибки с базой данных
- Убедитесь, что DATABASE_URL правильно настроен
- Проверьте, что миграции выполнены

### 2. Ошибки со статическими файлами
- Убедитесь, что директория `static/` существует
- Проверьте настройки STATIC_ROOT и STATICFILES_DIRS

### 3. CORS ошибки
- Добавьте домен фронтенда в CORS_ALLOWED_ORIGINS
- Проверьте настройки ALLOWED_HOSTS

## Полезные команды

```bash
# Просмотр логов
vercel logs

# Просмотр переменных окружения
vercel env ls

# Удаление развертывания
vercel remove
```

## Структура файлов для Vercel

```
project/
├── vercel.json          # Конфигурация Vercel (упрощенная)
├── requirements.txt     # Python зависимости
├── backend/
│   ├── wsgi.py         # WSGI приложение (обновлено для Vercel)
│   └── settings.py     # Настройки Django (обновлены)
└── static/             # Директория для статических файлов
```
