from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from .models import Skill
from urllib.parse import urlencode


def skill_list(request):
    skills = Skill.objects.all()
    return render(request, 'skills/index.html', {'skills': skills})


def skill_detail_redirect(request, skill_id):
    skill = get_object_or_404(Skill, id=skill_id)

    related_tags = skill.tags.all().values_list('name', flat=True)
    tags_string = ','.join(related_tags)
    query_params = urlencode({'tag': tags_string})

    return redirect(f"{reverse('project_list')}?{query_params}")
