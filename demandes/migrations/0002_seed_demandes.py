from django.db import migrations


def seed_demandes(apps, schema_editor):
    Demande = apps.get_model("demandes", "Demande")
    Demande.objects.create(
        name="Rénovation cuisine",
        owner="Claire",
        budget=8500,
        description="Modernisation d'une cuisine éco-responsable",
        impact="Faible émission",
        status="IN_PROGRESS",
    )
    Demande.objects.create(
        name="Isolation toiture",
        owner="Julien",
        budget=12000,
        description="Amélioration thermique d'un logement",
        impact="Économie d'énergie",
        status="PLANNED",
    )


def remove_seed_demandes(apps, schema_editor):
    Demande = apps.get_model("demandes", "Demande")
    Demande.objects.filter(name__in=["Rénovation cuisine", "Isolation toiture"]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("demandes", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_demandes, remove_seed_demandes),
    ]