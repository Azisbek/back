from rest_framework import serializers
from .models import (
    HeroSection, AboutSection, Partner, TeamMember, 
    Service, InsightCategory, Insight, ContactInfo, ContactMessage, ApplicationForm
)


class HeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSection
        fields = ['id', 'title', 'subtitle', 'description', 'background_image', 
                 'cta_text', 'cta_link', 'order']


class AboutSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutSection
        fields = ['id', 'title', 'description', 'image', 'mission', 'vision', 'values']


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ['id', 'name', 'logo', 'website', 'description', 'order']


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = ['id', 'name', 'position', 'bio', 'photo', 'email', 
                 'linkedin', 'twitter', 'order']


class ServiceSerializer(serializers.ModelSerializer):
    features_list = serializers.SerializerMethodField()
    
    class Meta:
        model = Service
        fields = ['id', 'title', 'description', 'short_description', 'icon', 
                 'price', 'features', 'features_list', 'is_featured', 'order']
    
    def get_features_list(self, obj):
        return obj.get_features_list()


class InsightCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = InsightCategory
        fields = ['id', 'name', 'slug', 'description']


class InsightListSerializer(serializers.ModelSerializer):
    category = InsightCategorySerializer(read_only=True)
    tags = serializers.SerializerMethodField()
    
    class Meta:
        model = Insight
        fields = ['id', 'title', 'slug', 'excerpt', 'featured_image', 
                 'category', 'author', 'tags', 'published_date', 'is_featured', 'views']
    
    def get_tags(self, obj):
        return obj.get_tags_list()


class InsightDetailSerializer(serializers.ModelSerializer):
    category = InsightCategorySerializer(read_only=True)
    tags = serializers.SerializerMethodField()
    
    class Meta:
        model = Insight
        fields = ['id', 'title', 'slug', 'excerpt', 'content', 'featured_image', 
                 'category', 'author', 'tags', 'published_date', 'updated_date', 
                 'is_featured', 'views']
    
    def get_tags(self, obj):
        return obj.get_tags_list()


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = ['id', 'company_name', 'address', 'phone', 'email', 'website', 
                 'working_hours', 'map_embed', 'facebook', 'instagram', 
                 'linkedin', 'twitter']


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['id', 'name', 'email', 'subject', 'message', 'phone']
        read_only_fields = ['id']

    def create(self, validated_data):
        return ContactMessage.objects.create(**validated_data)


class ApplicationFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationForm
        fields = ['id', 'full_name', 'phone', 'message']
        read_only_fields = ['id']

    def create(self, validated_data):
        return ApplicationForm.objects.create(**validated_data)

    def validate_phone(self, value):
        """Валидация номера телефона"""
        # Убираем все символы кроме цифр и +
        import re
        cleaned_phone = re.sub(r'[^\d+]', '', value)
        
        if len(cleaned_phone) < 10:
            raise serializers.ValidationError("Номер телефона слишком короткий")
        
        return value

    def validate_full_name(self, value):
        """Валидация ФИО"""
        if len(value.strip()) < 2:
            raise serializers.ValidationError("ФИО должно содержать минимум 2 символа")
        
        return value.strip()
