from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Tags field for easy user redirect for relevant projects
    tags = models.ManyToManyField('projects.Tag', related_name='skills', blank=True)

    def __str__(self):
        return self.name
