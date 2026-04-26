from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Profile, Experience, Skill, SkillCategory, Project, ContactMessage, SocialLink


def home(request):
    profile = Profile.objects.filter(is_active=True).first()
    social_links = SocialLink.objects.filter(is_active=True).order_by('order')
    featured_projects = Project.objects.filter(is_featured=True, is_active=True)[:3]
    return render(request, 'core/home.html', {
        'profile': profile,
        'social_links': social_links,
        'featured_projects': featured_projects,
    })


def about(request):
    profile = Profile.objects.filter(is_active=True).first()
    social_links = SocialLink.objects.filter(is_active=True).order_by('order')
    return render(request, 'core/about.html', {
        'profile': profile,
        'social_links': social_links,
    })


def experience(request):
    profile = Profile.objects.filter(is_active=True).first()
    experiences = Experience.objects.filter(is_active=True).order_by('-start_date')
    return render(request, 'core/experience.html', {
        'profile': profile,
        'experiences': experiences,
    })


def skills(request):
    profile = Profile.objects.filter(is_active=True).first()
    categories = SkillCategory.objects.all()
    skills_by_category = {}
    for category in categories:
        skills_by_category[category] = Skill.objects.filter(
            category=category, is_active=True
        ).order_by('order')
    uncat_skills = Skill.objects.filter(category__isnull=True, is_active=True).order_by('order')
    return render(request, 'core/skills.html', {
        'profile': profile,
        'categories': categories,
        'skills_by_category': skills_by_category,
        'uncat_skills': uncat_skills,
    })


def project(request):
    profile = Profile.objects.filter(is_active=True).first()
    projects = Project.objects.filter(is_active=True).order_by('order')
    social_links = SocialLink.objects.filter(is_active=True).order_by('order')
    return render(request, 'core/project.html', {
        'profile': profile,
        'projects': projects,
        'social_links': social_links,
    })


def contact(request):
    profile = Profile.objects.filter(is_active=True).first()
    social_links = SocialLink.objects.filter(is_active=True).order_by('order')
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        contact_msg = ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )
        
        try:
            if settings.EMAIL_HOST_USER and settings.DEFAULT_FROM_EMAIL:
                send_mail(
                    f"Portfolio Contact: {name} - {subject}",
                    f"From: {name} <{email}>\n\nSubject: {subject}\n\nMessage:\n{message}",
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.DEFAULT_FROM_EMAIL],
                    fail_silently=False,
                )
            messages.success(request, 'Your message has been sent successfully!')
        except Exception as e:
            print(f"Email error: {e}")
            messages.success(request, 'Your message has been saved! We will get back to you soon.')
        
        return redirect('contact')
    
    return render(request, 'core/contact.html', {
        'profile': profile,
        'social_links': social_links,
    })