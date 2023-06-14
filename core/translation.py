from modeltranslation.translator import register, TranslationOptions
from core import models


@register(models.Profile)
class ProfileTranslationOptions(TranslationOptions):
    fields = ('description',)


@register(models.Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)


@register(models.ProfessionalExperience)
class ProfessionalExperienceTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)
