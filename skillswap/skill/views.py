from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def skill_list(request):
    skill= Skill.objects.all()
    return render(request, 'skill/skill_list.html',{'skills': skill})
@login_required
def skill_add(request):
    if request.method =="POST":
        form= SkillForm(request.POST)
        if form.is_valid():
            skill=form.save(commit=False)
            skill.user= request.user
            skill.save()
            return redirect('skill_list')
    else:
        form = SkillForm()
    return render(request, 'skill/skill_add.html', {'form': form})
        
# @login_required
# def skill_detail(request, skill_id):
#     skill = get_object_or_404(Skill, id= skill_id)
#     return render(request, 'skill/skill_detail.html', {'skill': skill}) 
