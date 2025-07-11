from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from skill.models import Skill

def skill_search(request):
    title = request.GET.get('title')
    location = request.GET.get('location')
    category = request.GET.get('category')
    skill_type = request.GET.get('skill_type')
    availability = request.GET.get('availability')

    skills = Skill.objects.all()

    filters = Q()
    if title:
        filters &= Q(title__icontains=title)
    if location:
        filters &= Q(location__icontains=location)
    if category:
        filters &= Q(category__icontains=category)
    if skill_type:
        filters &= Q(skill_type__icontains=skill_type)
    if availability:
        filters &= Q(availability__icontains=availability)

    skills = skills.filter(filters)

    all_categories = Skill.objects.values_list('category', flat=True).distinct()
    all_locations = Skill.objects.values_list('location', flat=True).distinct()
    all_types = Skill.objects.values_list('skill_type', flat=True).distinct()
    all_availabilities = Skill.objects.values_list('availability', flat=True).distinct()

    return render(request, 'skill/skill_search.html', {
        'skills': skills,
        'all_categories': all_categories,
        'all_locations': all_locations,
        'all_types': all_types,
        'all_availabilities': all_availabilities,
    })
