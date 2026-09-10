from django.db import models


class ProjectStatus(models.TextChoices):
    PLANNED = "PLANNED", "Planifié"
    IN_PROGRESS = "IN_PROGRESS", "En cours"
    COMPLETED = "COMPLETED", "Terminé"


class Project(models.Model):
    name = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, default="")
    impact = models.CharField(max_length=255, default="Impact estimé à calculer")
    status = models.CharField(
        max_length=20,
        choices=ProjectStatus.choices,
        default=ProjectStatus.PLANNED,
    )

    def __str__(self):
        return self.name
