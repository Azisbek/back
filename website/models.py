from django.db import models
from ckeditor.fields import RichTextField


class HeroSection(models.Model):
    """Главная секция (Hero)"""
    title = models.CharField('Заголовок', max_length=200)
    subtitle = models.CharField('Подзаголовок', max_length=300, blank=True)
    description = models.TextField('Описание', blank=True)
    background_image = models.ImageField('Фоновое изображение', upload_to='hero/', blank=True)
    cta_text = models.CharField('Текст кнопки', max_length=100, blank=True)
    cta_link = models.CharField('Ссылка кнопки', max_length=500, blank=True)
    is_active = models.BooleanField('Активно', default=True)
    order = models.PositiveIntegerField('Порядок', default=0)

    class Meta:
        verbose_name = 'Главная секция'
        verbose_name_plural = 'Главные секции'
        ordering = ['order']

    def __str__(self):
        return self.title


class AboutSection(models.Model):
    """Секция О нас"""
    title = models.CharField('Заголовок', max_length=200)
    description = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='about/', blank=True)
    mission = models.TextField('Миссия', blank=True)
    vision = models.TextField('Видение', blank=True)
    values = models.TextField('Ценности', blank=True)
    is_active = models.BooleanField('Активно', default=True)

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

    def __str__(self):
        return self.title


class Partner(models.Model):
    """Партнер"""
    name = models.CharField('Название', max_length=200)
    logo = models.ImageField('Логотип', upload_to='partners/')
    website = models.CharField('Сайт', max_length=500, blank=True)
    description = models.TextField('Описание', blank=True)
    is_active = models.BooleanField('Активно', default=True)
    order = models.PositiveIntegerField('Порядок', default=0)

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    """Член команды"""
    name = models.CharField('Имя', max_length=200)
    position = models.CharField('Должность', max_length=200)
    bio = models.TextField('Биография', blank=True)
    photo = models.ImageField('Фото', upload_to='team/')
    email = models.EmailField('Email', blank=True)
    linkedin = models.CharField('LinkedIn', max_length=500, blank=True)
    twitter = models.CharField('Twitter', max_length=500, blank=True)
    is_active = models.BooleanField('Активно', default=True)
    order = models.PositiveIntegerField('Порядок', default=0)

    class Meta:
        verbose_name = 'Член команды'
        verbose_name_plural = 'Команда'
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} - {self.position}"


class Service(models.Model):
    """Услуга"""
    title = models.CharField('Название', max_length=200)
    description = models.TextField('Описание')
    short_description = models.CharField('Краткое описание', max_length=300, blank=True)
    icon = models.ImageField('Иконка', upload_to='services/', blank=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2, blank=True, null=True)
    features = models.TextField('Особенности', blank=True, help_text='Разделите особенности новой строкой')
    is_active = models.BooleanField('Активно', default=True)
    is_featured = models.BooleanField('Рекомендуемая', default=False)
    order = models.PositiveIntegerField('Порядок', default=0)

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['order', 'title']

    def __str__(self):
        return self.title

    def get_features_list(self):
        """Возвращает список особенностей"""
        if self.features:
            return [feature.strip() for feature in self.features.split('\n') if feature.strip()]
        return []


class InsightCategory(models.Model):
    """Категория статей"""
    name = models.CharField('Название', max_length=100)
    slug = models.SlugField('Слаг', unique=True)
    description = models.TextField('Описание', blank=True)

    class Meta:
        verbose_name = 'Категория статей'
        verbose_name_plural = 'Категории статей'

    def __str__(self):
        return self.name


class Insight(models.Model):
    """Статья/Инсайт"""
    title = models.CharField('Заголовок', max_length=200)
    slug = models.SlugField('Слаг', unique=True)
    excerpt = models.TextField('Краткое описание', max_length=500)
    content = RichTextField('Содержание')
    featured_image = models.ImageField('Главное изображение', upload_to='insights/')
    category = models.ForeignKey(InsightCategory, on_delete=models.CASCADE, verbose_name='Категория')
    author = models.CharField('Автор', max_length=200)
    tags = models.CharField('Теги', max_length=500, blank=True, help_text='Теги через запятую')
    published_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    updated_date = models.DateTimeField('Дата обновления', auto_now=True)
    is_published = models.BooleanField('Опубликовано', default=True)
    is_featured = models.BooleanField('Рекомендуемая', default=False)
    views = models.PositiveIntegerField('Просмотры', default=0)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_date']

    def __str__(self):
        return self.title

    def get_tags_list(self):
        """Возвращает список тегов"""
        if self.tags:
            return [tag.strip() for tag in self.tags.split(',') if tag.strip()]
        return []


class ContactInfo(models.Model):
    """Контактная информация"""
    company_name = models.CharField('Название компании', max_length=200)
    address = models.TextField('Адрес')
    phone = models.CharField('Телефон', max_length=50)
    email = models.EmailField('Email')
    website = models.CharField('Сайт', max_length=500, blank=True)
    working_hours = models.TextField('Часы работы', blank=True)
    map_embed = models.TextField('Код карты', blank=True, help_text='HTML код для встраивания карты')
    
    # Социальные сети
    facebook = models.CharField('Facebook', max_length=500, blank=True)
    instagram = models.CharField('Instagram', max_length=500, blank=True)
    linkedin = models.CharField('LinkedIn', max_length=500, blank=True)
    twitter = models.CharField('Twitter', max_length=500, blank=True)
    
    is_active = models.BooleanField('Активно', default=True)

    class Meta:
        verbose_name = 'Контактная информация'
        verbose_name_plural = 'Контактная информация'

    def __str__(self):
        return self.company_name


class ContactMessage(models.Model):
    """Сообщение с формы обратной связи"""
    name = models.CharField('Имя', max_length=200)
    email = models.EmailField('Email')
    subject = models.CharField('Тема', max_length=300, blank=True)
    message = models.TextField('Сообщение')
    phone = models.CharField('Телефон', max_length=50, blank=True)
    created_date = models.DateTimeField('Дата создания', auto_now_add=True)
    is_read = models.BooleanField('Прочитано', default=False)
    is_replied = models.BooleanField('Отвечено', default=False)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['-created_date']

    def __str__(self):
        return f"{self.name} - {self.subject or 'Без темы'}"


class ApplicationForm(models.Model):
    """Форма заявки"""
    full_name = models.CharField('ФИО', max_length=300)
    phone = models.CharField('Номер телефона', max_length=50)
    message = models.TextField('Сообщение')
    created_date = models.DateTimeField('Дата создания', auto_now_add=True)
    is_processed = models.BooleanField('Обработано', default=False)
    is_contacted = models.BooleanField('Связались', default=False)
    notes = models.TextField('Заметки менеджера', blank=True)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-created_date']

    def __str__(self):
        return f"{self.full_name} - {self.phone}"
