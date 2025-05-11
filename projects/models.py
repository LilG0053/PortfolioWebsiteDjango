from django.db import models
# Project models


# Tag model for easy project sorting
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# Project model to showcase projects
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='projects') # Related_name allows getting Projects from Tag
    image = models.ImageField(upload_to='project_images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
