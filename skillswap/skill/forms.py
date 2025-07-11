
from django import forms
from .models import Skill

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['title', 'category', 'description', 'availability', 'location', 'skill_type']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
