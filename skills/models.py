from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Projects field to show use of skills
    projects = models.ManyToManyField('projects.Project', related_name='skills', blank=True)

    def __str__(self):
        return self.name

