import os
import uuid
from django.db import models
from core.utils.files import generate_unique_filename
from django.utils.translation import gettext_lazy as _


def images_path(instance: models.Model, filename: str) -> str:
    model_name = instance._meta.verbose_name_plural.lower().replace(' ', '_')
    unique_filename = generate_unique_filename(filename)
    return os.path.join('images', model_name, unique_filename)


class Profile(models.Model):
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profile'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=images_path)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Technology(models.Model):
    class Meta:
        verbose_name = 'Technology'
        verbose_name_plural = 'Technologies'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    image = models.FileField(upload_to=images_path)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ProfessionalExperience(models.Model):
    class Meta:
        verbose_name = 'Professional Experience'
        verbose_name_plural = 'Professional Experiences'
        unique_together = ('name', 'company', 'start_date', 'end_date')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to=images_path)
    repository = models.URLField()
    description = models.TextField()
    technologies = models.ManyToManyField(Technology)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Institution(models.Model):
    class Meta:
        verbose_name = 'Institution'
        verbose_name_plural = 'Institutions'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    image = models.FileField(upload_to=images_path)
    site = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Formation(models.Model):
    class Meta:
        verbose_name = 'Formation'
        verbose_name_plural = 'Formations'

    status_choices = (
        ('Completed', _('Completed')),
        ('Incomplete', _('Incomplete')),
        ('Suspended', _('Suspended')),
        ('Ongoing', _('Ongoing')),
    )

    degree_choices = (
        ('High School', _('High School')),
        ('Technical', _('Technical')),
        ('Graduation', _('Graduation')),
        ('Postgraduate', _('Postgraduate')),
        ('Doctorate', _('Doctorate')),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    degree = models.CharField(max_length=100, choices=degree_choices)
    institution = models.ForeignKey(
        Institution, on_delete=models.SET_NULL, null=True
    )
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=100, choices=status_choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    institution = models.ForeignKey(
        Institution, on_delete=models.SET_NULL, null=True)
    workload = models.IntegerField()
    certification_date = models.DateField()
    certificate_link = models.URLField()
    image = models.ImageField(upload_to=images_path, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class SocialLink(models.Model):
    class Meta:
        verbose_name = 'Social Link'
        verbose_name_plural = 'Social Links'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    image = models.FileField(upload_to=images_path)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Skill(models.Model):
    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
