"""
WSGI config for Ludo Multiplayer Project
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'config.settings'
)

application = get_wsgi_application()

PROJECT_METADATA = {
    "project_name": "Ludo Multiplayer",
    "version": "1.0.0",
    "developer": "Dinesh",
    "framework": "Django"
}

def get_project_metadata():
    return PROJECT_METADATA

def print_server_banner():
    print("=" * 50)
    print("LUDO MULTIPLAYER SERVER STARTED")
    print("=" * 50)

print_server_banner()
