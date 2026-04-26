from django.contrib import admin
from .models import (
    Profile, Experience, SkillCategory, Skill, 
    Project, ContactMessage, SocialLink
)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'email', 'is_active', 'created_at']
    list_filter = ['is_active']
    search_fields = ['name', 'title', 'bio']


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['company', 'position', 'start_date', 'end_date', 'is_current', 'order']
    list_filter = ['is_current', 'is_active']
    search_fields = ['company', 'position', 'description']
    list_editable = ['order']


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'order']
    list_editable = ['order']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency_level', 'order', 'is_active']
    list_filter = ['category', 'is_active']
    search_fields = ['name']
    list_editable = ['order', 'proficiency_level']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_featured', 'order', 'is_active', 'created_at']
    list_filter = ['is_featured', 'is_active']
    search_fields = ['title', 'description', 'tech_stack']
    list_editable = ['order', 'is_featured']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'is_read', 'created_at']
    list_filter = ['is_read']
    search_fields = ['name', 'email', 'message']
    list_editable = ['is_read']
    readonly_fields = ['created_at']


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'url', 'order', 'is_active']
    list_filter = ['is_active']
    list_editable = ['order', 'is_active']