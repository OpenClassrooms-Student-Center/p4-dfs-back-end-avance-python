from django.db import migrations


def seed_projects(apps, schema_editor):
    Project = apps.get_model("projects", "Project")
    Project.objects.create(
        name="Rénovation cuisine",
        owner="Claire",
        budget=8500,
        description="Modernisation d'une cuisine éco-responsable",
        impact="Faible émission",
        status="IN_PROGRESS",
    )
    Project.objects.create(
        name="Isolation toiture",
        owner="Julien",
        budget=12000,
        description="Amélioration thermique d'un logement",
        impact="Économie d'énergie",
        status="PLANNED",
    )


def remove_seed_projects(apps, schema_editor):
    Project = apps.get_model("projects", "Project")
    Project.objects.filter(name__in=["Rénovation cuisine", "Isolation toiture"]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_projects, remove_seed_projects),
    ]
