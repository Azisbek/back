from django.contrib import admin
from django.utils.html import format_html
from .models import (
    HeroSection, AboutSection, Partner, TeamMember, 
    Service, InsightCategory, Insight, ContactInfo, ContactMessage, ApplicationForm
)


@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'is_active', 'order']
    list_filter = ['is_active']
    search_fields = ['title', 'subtitle']
    list_editable = ['is_active', 'order']
    ordering = ['order']

    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'subtitle', 'description')
        }),
        ('Изображения и ссылки', {
            'fields': ('background_image', 'cta_text', 'cta_link')
        }),
        ('Настройки', {
            'fields': ('is_active', 'order')
        }),
    )


@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']
    list_filter = ['is_active']
    search_fields = ['title']

    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'description', 'image')
        }),
        ('Дополнительная информация', {
            'fields': ('mission', 'vision', 'values')
        }),
        ('Настройки', {
            'fields': ('is_active',)
        }),
    )


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'website', 'is_active', 'order']
    list_filter = ['is_active']
    search_fields = ['name']
    list_editable = ['is_active', 'order']
    ordering = ['order', 'name']

    def logo_preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" width="50" height="50" />', obj.logo.url)
        return "Нет изображения"
    logo_preview.short_description = 'Превью логотипа'

    readonly_fields = ['logo_preview']
    fields = ['name', 'logo', 'logo_preview', 'website', 'description', 'is_active', 'order']


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'email', 'is_active', 'order']
    list_filter = ['is_active', 'position']
    search_fields = ['name', 'position', 'email']
    list_editable = ['is_active', 'order']
    ordering = ['order', 'name']

    def photo_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 50%;" />', obj.photo.url)
        return "Нет фото"
    photo_preview.short_description = 'Превью фото'

    readonly_fields = ['photo_preview']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'position', 'bio', 'photo', 'photo_preview')
        }),
        ('Контакты', {
            'fields': ('email', 'linkedin', 'twitter')
        }),
        ('Настройки', {
            'fields': ('is_active', 'order')
        }),
    )


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'is_active', 'is_featured', 'order']
    list_filter = ['is_active', 'is_featured']
    search_fields = ['title', 'description']
    list_editable = ['is_active', 'is_featured', 'order']
    ordering = ['order', 'title']

    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'description', 'short_description', 'icon')
        }),
        ('Цена и особенности', {
            'fields': ('price', 'features')
        }),
        ('Настройки', {
            'fields': ('is_active', 'is_featured', 'order')
        }),
    )


@admin.register(InsightCategory)
class InsightCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Insight)
class InsightAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'author', 'published_date', 'is_published', 'is_featured', 'views']
    list_filter = ['category', 'is_published', 'is_featured', 'published_date']
    search_fields = ['title', 'excerpt', 'author']
    list_editable = ['is_published', 'is_featured']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_date'
    ordering = ['-published_date']

    def featured_image_preview(self, obj):
        if obj.featured_image:
            return format_html('<img src="{}" width="100" height="60" />', obj.featured_image.url)
        return "Нет изображения"
    featured_image_preview.short_description = 'Превью изображения'

    readonly_fields = ['featured_image_preview', 'views', 'published_date', 'updated_date']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'slug', 'category', 'author')
        }),
        ('Содержание', {
            'fields': ('excerpt', 'content', 'featured_image', 'featured_image_preview'),
            'description': 'Используйте редактор для форматирования текста. Поддерживаются изображения, таблицы, списки и многое другое.'
        }),
        ('Теги и категории', {
            'fields': ('tags',),
            'description': 'Введите теги через запятую (например: Инвестиции, ESG, Устойчивое развитие)'
        }),
        ('Настройки публикации', {
            'fields': ('is_published', 'is_featured')
        }),
        ('Статистика', {
            'fields': ('views', 'published_date', 'updated_date'),
            'classes': ('collapse',)
        }),
    )


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'phone', 'email', 'is_active']
    list_filter = ['is_active']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('company_name', 'address', 'phone', 'email', 'website', 'working_hours')
        }),
        ('Социальные сети', {
            'fields': ('facebook', 'instagram', 'linkedin', 'twitter')
        }),
        ('Карта', {
            'fields': ('map_embed',)
        }),
        ('Настройки', {
            'fields': ('is_active',)
        }),
    )


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_date', 'is_read', 'is_replied']
    list_filter = ['is_read', 'is_replied', 'created_date']
    search_fields = ['name', 'email', 'subject', 'message']
    list_editable = ['is_read', 'is_replied']
    readonly_fields = ['created_date']
    ordering = ['-created_date']
    
    fieldsets = (
        ('Информация об отправителе', {
            'fields': ('name', 'email', 'phone')
        }),
        ('Сообщение', {
            'fields': ('subject', 'message', 'created_date')
        }),
        ('Статус', {
            'fields': ('is_read', 'is_replied')
        }),
    )

    def has_add_permission(self, request):
        # Запрещаем добавление сообщений через админку
        return False


@admin.register(ApplicationForm)
class ApplicationFormAdmin(admin.ModelAdmin):
    # Основные настройки отображения
    list_display = [
        'full_name', 'phone', 'short_message', 'created_date', 
        'status_display', 'is_processed', 'is_contacted'
    ]
    
    # Расширенные фильтры
    list_filter = [
        'is_processed', 
        'is_contacted', 
        ('created_date', admin.DateFieldListFilter),
        'created_date',
    ]
    
    # Расширенный поиск
    search_fields = [
        'full_name', 'phone', 'message', 'notes'
    ]
    
    # Поля для быстрого редактирования
    list_editable = ['is_processed', 'is_contacted']
    
    # Поля только для чтения
    readonly_fields = ['created_date', 'message_preview']
    
    # Сортировка по умолчанию
    ordering = ['-created_date']
    
    # Количество записей на странице
    list_per_page = 25
    list_max_show_all = 100
    
    # Группировка полей в форме редактирования
    fieldsets = (
        ('📋 Информация о заявителе', {
            'fields': ('full_name', 'phone', 'created_date'),
            'classes': ('wide',)
        }),
        ('💬 Сообщение', {
            'fields': ('message', 'message_preview'),
            'classes': ('wide',)
        }),
        ('⚙️ Статус обработки', {
            'fields': ('is_processed', 'is_contacted', 'notes'),
            'classes': ('wide',)
        }),
    )

    def has_add_permission(self, request):
        # Запрещаем добавление заявок через админку
        return False

    # Кастомные методы для отображения
    def short_message(self, obj):
        """Краткое сообщение для списка"""
        if len(obj.message) > 50:
            return obj.message[:50] + '...'
        return obj.message
    short_message.short_description = 'Сообщение'
    
    def status_display(self, obj):
        """Цветной статус"""
        if obj.is_processed and obj.is_contacted:
            return format_html(
                '<span style="color: green; font-weight: bold;">✅ Завершено</span>'
            )
        elif obj.is_processed:
            return format_html(
                '<span style="color: orange; font-weight: bold;">🔄 Обработано</span>'
            )
        elif obj.is_contacted:
            return format_html(
                '<span style="color: blue; font-weight: bold;">📞 Связались</span>'
            )
        else:
            return format_html(
                '<span style="color: red; font-weight: bold;">🆕 Новая</span>'
            )
    status_display.short_description = 'Статус'
    status_display.admin_order_field = 'is_processed'
    
    def message_preview(self, obj):
        """Превью сообщения в форме редактирования"""
        return format_html(
            '<div style="background: #f8f9fa; padding: 10px; border-radius: 5px; max-height: 200px; overflow-y: auto;">{}</div>',
            obj.message
        )
    message_preview.short_description = 'Превью сообщения'

    # Расширенные действия для массовой обработки
    actions = [
        'mark_as_processed', 
        'mark_as_contacted', 
        'mark_as_completed',
        'export_as_csv',
        'reset_status'
    ]

    def mark_as_processed(self, request, queryset):
        updated = queryset.update(is_processed=True)
        self.message_user(request, f'✅ {updated} заявок отмечено как обработанные.')
    mark_as_processed.short_description = '✅ Отметить как обработанные'

    def mark_as_contacted(self, request, queryset):
        updated = queryset.update(is_contacted=True)
        self.message_user(request, f'📞 С {updated} заявителями отмечено, что связались.')
    mark_as_contacted.short_description = '📞 Отметить что связались'
    
    def mark_as_completed(self, request, queryset):
        updated = queryset.update(is_processed=True, is_contacted=True)
        self.message_user(request, f'🎉 {updated} заявок отмечено как полностью завершенные.')
    mark_as_completed.short_description = '🎉 Отметить как завершенные'
    
    def reset_status(self, request, queryset):
        updated = queryset.update(is_processed=False, is_contacted=False)
        self.message_user(request, f'🔄 Статус {updated} заявок сброшен.')
    reset_status.short_description = '🔄 Сбросить статус'
    
    def export_as_csv(self, request, queryset):
        """Экспорт выбранных заявок в CSV"""
        import csv
        from django.http import HttpResponse
        from datetime import datetime
        
        response = HttpResponse(content_type='text/csv; charset=utf-8')
        response['Content-Disposition'] = f'attachment; filename="applications_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv"'
        
        # Добавляем BOM для корректного отображения в Excel
        response.write('\ufeff')
        
        writer = csv.writer(response)
        writer.writerow([
            'ФИО', 'Телефон', 'Сообщение', 'Дата создания', 
            'Обработано', 'Связались', 'Заметки'
        ])
        
        for obj in queryset:
            writer.writerow([
                obj.full_name,
                obj.phone,
                obj.message,
                obj.created_date.strftime('%Y-%m-%d %H:%M:%S'),
                'Да' if obj.is_processed else 'Нет',
                'Да' if obj.is_contacted else 'Нет',
                obj.notes or ''
            ])
        
        return response
    export_as_csv.short_description = '📊 Экспорт в CSV'

    # Кастомные фильтры
    def get_list_filter(self, request):
        """Динамические фильтры"""
        filters = list(self.list_filter)
        
        # Добавляем фильтр по статусу
        class StatusFilter(admin.SimpleListFilter):
            title = 'Статус заявки'
            parameter_name = 'status'

            def lookups(self, request, model_admin):
                return (
                    ('new', '🆕 Новые'),
                    ('processed', '🔄 Обработанные'),
                    ('contacted', '📞 Связались'),
                    ('completed', '✅ Завершенные'),
                )

            def queryset(self, request, queryset):
                if self.value() == 'new':
                    return queryset.filter(is_processed=False, is_contacted=False)
                elif self.value() == 'processed':
                    return queryset.filter(is_processed=True, is_contacted=False)
                elif self.value() == 'contacted':
                    return queryset.filter(is_processed=False, is_contacted=True)
                elif self.value() == 'completed':
                    return queryset.filter(is_processed=True, is_contacted=True)
        
        filters.append(StatusFilter)
        return filters

    # Кастомный заголовок для админки
    def changelist_view(self, request, extra_context=None):
        """Добавляем статистику в заголовок"""
        extra_context = extra_context or {}
        
        # Получаем статистику
        total = ApplicationForm.objects.count()
        new = ApplicationForm.objects.filter(is_processed=False, is_contacted=False).count()
        processed = ApplicationForm.objects.filter(is_processed=True, is_contacted=False).count()
        contacted = ApplicationForm.objects.filter(is_processed=False, is_contacted=True).count()
        completed = ApplicationForm.objects.filter(is_processed=True, is_contacted=True).count()
        
        extra_context['statistics'] = {
            'total': total,
            'new': new,
            'processed': processed,
            'contacted': contacted,
            'completed': completed
        }
        
        return super().changelist_view(request, extra_context)


# Настройка заголовков админки
admin.site.site_header = 'Администрирование сайта'
admin.site.site_title = 'Админ панель'
admin.site.index_title = 'Управление контентом сайта'
