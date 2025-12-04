from django.urls import path
from . import views

urlpatterns = [
    # Получение всех данных одним запросом
    path('website-data/', views.website_data, name='website_data'),
    
    # Hero секции
    path('hero/', views.HeroSectionListView.as_view(), name='hero_list'),
    
    # О нас
    path('about/', views.AboutSectionView.as_view(), name='about'),
    
    # Партнеры
    path('partners/', views.PartnerListView.as_view(), name='partners'),
    
    # Команда
    path('team/', views.TeamListView.as_view(), name='team'),
    
    # Услуги
    path('services/', views.ServiceListView.as_view(), name='services'),
    path('services/featured/', views.FeaturedServiceListView.as_view(), name='featured_services'),
    
    # Статьи/Инсайты
    path('insights/categories/', views.InsightCategoryListView.as_view(), name='insight_categories'),
    path('insights/tags/', views.insight_tags_list, name='insight_tags'),
    path('insights/', views.InsightListView.as_view(), name='insights'),
    path('insights/<slug:slug>/', views.InsightDetailView.as_view(), name='insight_detail'),
    
    # Контакты
    path('contact/', views.ContactInfoView.as_view(), name='contact_info'),
    path('contact/message/', views.ContactMessageCreateView.as_view(), name='contact_message'),
    
    # Заявки
    path('application/', views.ApplicationFormCreateView.as_view(), name='application_form'),
]
