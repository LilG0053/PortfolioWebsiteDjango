from django.shortcuts import render
from .models import Project, Tag



def project_list(request):
    # Get all tags to display in the filter section
    tags = Tag.objects.all()

    # Get the search query and tag filter from the request
    search_query = request.GET.get('search', '')
    selected_tag = request.GET.get('tag', None)

    # Start with all projects
    projects = Project.objects.all()

    # Filter by selected tag if provided, None tag is referred to as a string
    if selected_tag and str(selected_tag) != 'None':
        projects = projects.filter(tags__name=selected_tag)
        print(f"Selected tag: {selected_tag}")

    # Filter by search query if provided
    if search_query:
        projects = projects.filter(title__icontains=search_query) | projects.filter(description__icontains=search_query)

    return render(request, 'projects/index.html', {
        'projects': projects,
        'tags': tags,
        'selected_tag': selected_tag,
        'search_query': search_query
    })

