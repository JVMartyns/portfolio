from django.conf import settings
from django.contrib import messages
from django.core.cache import cache
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.db.models import Prefetch
from django.utils import translation
from django.utils.translation import gettext_lazy as _
from core import forms, models


def index(request):
    technologies = models.Technology.objects.all()\
        .order_by('order')

    social_links = models.SocialLink.objects.all()
    cache.set('social_links', social_links)

    profile = models.Profile.objects.first()

    context = {
        'profile': profile,
        'technologies': technologies,
    }

    return render(request, 'core/index.html', context)


def formation(request):
    formations = models.Formation.objects.all()\
        .order_by('-end_date')
    courses = models.Course.objects.all()\
        .order_by('-certification_date')

    context = {
        'formations': formations,
        'courses': courses
    }
    return render(request, 'core/formation.html', context)


def experience(request):
    experiences = models.ProfessionalExperience.objects.all()\
        .order_by('-end_date')

    context = {
        'experiences': experiences,
    }

    return render(request, 'core/experience.html', context)


def projects(request):
    technologies = models.Technology.objects.all().order_by('order')
    projects = models.Project.objects.all()\
        .order_by('order')\
        .prefetch_related(Prefetch('technologies', queryset=technologies))

    context = {
        'projects': projects,
    }

    return render(request, 'core/projects.html', context)


def send_contact_email(form: forms.ContactForm):
    subject = form.cleaned_data.get("subject", "")
    name = form.cleaned_data.get("name", "")
    sender = f'{name} <{form.cleaned_data.get("email", "")}>'
    message = form.cleaned_data.get("message", "")
    recipients = [settings.DEFAULT_RECEIVER]
    return send_mail(subject, message, sender, recipients)


def contact(request):
    form = forms.ContactForm()
    social_links = models.SocialLink.objects.all()

    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            if send_contact_email(form):
                messages.success(request, _('Message sent successfully!'))
                return redirect('core:contact')
            messages.error(request, _('Message failed to send!'))
        else:
            messages.warning(request, _('Please correct the errors below.'))

    context = {'form': form, 'social_links': social_links}
    return render(request, 'core/contact.html', context)


def set_language(request):
    if request.method == 'POST':
        language_code = request.POST.get('language')
        if language_code:
            translation.activate(language_code)
            response = redirect(request.META.get('HTTP_REFERER'))
            response.set_cookie('django_language', language_code)
            return response


def set_theme(request):
    if request.method == 'POST':
        theme = request.POST.get('theme')
        if theme:
            response = redirect(request.META.get('HTTP_REFERER'))
            response.set_cookie('django_theme', theme)
            return response
