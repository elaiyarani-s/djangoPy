from django.shortcuts import render, redirect, get_object_or_404
from .models import Skill, Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from typing import cast


def skill_list(request):
    skills = Skill.objects.all()
    return render(request, 'skills/skill_list.html', {'skills': skills})


@login_required
def skill_create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.user = request.user
            skill.save()
            return redirect('skills:detail', pk=skill.pk)
    else:
        form = ReviewForm()
    return render(request, 'skills/skill_form.html', {'form': form})


def skill_detail(request, pk: int):
    skill = cast(Skill, get_object_or_404(Skill, pk=pk))
    reviews = skill.reviews.all()
    can_review = request.user.is_authenticated and request.user != skill.user

    if request.method == 'POST' and can_review:
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.skill = skill
            review.user = request.user
            review.save()
            return redirect('skills:detail', pk=skill.pk)
    else:
        form = ReviewForm()

    return render(request, 'skills/detail.html', {
        'skill': skill,
        'reviews': reviews,
        'form': form,
        'can_review': can_review
    })