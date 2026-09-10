from rest_framework import status
from rest_framework.test import APITestCase


class ProjectAPITests(APITestCase):
    def test_should_list_projects(self):
        response = self.client.get("/api/projects/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_should_create_project(self):
        payload = {
            "name": "Isolation double vitrage",
            "owner": "Sophie",
            "budget": 6000,
            "description": "Travaux complémentaires",
            "impact": "Très bon",
            "status": "PLANNED",
        }
        response = self.client.post("/api/projects/", payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], "Isolation double vitrage")

    def test_should_reject_project_without_owner(self):
        payload = {"name": "Sans client", "owner": "", "budget": 1000}
        response = self.client.post("/api/projects/", payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_should_return_404_for_unknown_project(self):
        response = self.client.get("/api/projects/999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
