from rest_framework import serializers

from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "name", "owner", "budget", "description", "impact", "status"]

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Le nom du projet est obligatoire")
        return value

    def validate_owner(self, value):
        if not value.strip():
            raise serializers.ValidationError("Le nom du client est obligatoire")
        return value

    def validate_budget(self, value):
        if value <= 0:
            raise serializers.ValidationError("Le budget doit être positif")
        return value
