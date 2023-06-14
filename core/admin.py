from django.contrib import admin
from core import models


@admin.register(models.Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'order', 'image',
        'created_at', 'updated_at'
    )
    list_editable = ('order',)
    ordering = ('order',)


@admin.register(models.ProfessionalExperience)
class ProfessionalExperienceAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'start_date', 'end_date',
        'created_at', 'updated_at'
    )
    ordering = ('-end_date',)


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'image', 'order',
        'created_at', 'updated_at'
    )
    list_editable = ('order',)
    ordering = ('order',)


@admin.register(models.Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'image', 'created_at', 'updated_at'
    )
    ordering = ('-created_at',)


@admin.register(models.Formation)
class FormationAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'institution',
        'start_date', 'end_date',
        'created_at', 'updated_at'
    )
    ordering = ('-end_date',)


@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'institution',
        'certification_date',
        'created_at', 'updated_at'
    )
    ordering = ('-certification_date',)


@admin.register(models.SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'url',
        'created_at', 'updated_at'
    )
    ordering = ('-created_at',)
