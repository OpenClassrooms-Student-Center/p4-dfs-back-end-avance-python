# EcoReno

Application de gestion de demandes de rénovation écologique : API REST (Django REST Framework) et interface web simple pour suivre les demandes d'un client (nom, budget, description, impact estimé, statut).

## Prérequis

- Python 3.14+
- pip

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
```

## Lancement

```bash
python manage.py runserver
```

L'application est disponible sur http://localhost:8000/ et l'API sur http://localhost:8000/api/demandes/.

## Tests

```bash
python manage.py test
```

## Stack technique

- Python 3.14
- Django 6.x + Django REST Framework
- SQLite

## Structure du projet

- `ecoreno/` : configuration du projet Django (settings, urls, WSGI/ASGI)
- `demandes/` : application métier (modèles, serializers, vues, tests)
- `templates/index.html` : interface web

## API Endpoints

| Méthode | Endpoint | Description |
| --- | --- | --- |
| GET | `/api/demandes/` | Liste des demandes |
| POST | `/api/demandes/` | Création d'une demande |
| GET | `/api/demandes/{id}/` | Détail d'une demande |
| PUT | `/api/demandes/{id}/` | Mise à jour d'une demande |

## Licence

Usage interne.
