"""
Ludo Game Project Configuration Package
"""

__version__ = "1.0.0"
__author__ = "Dinesh"
__project__ = "Ludo Multiplayer"

PROJECT_STATUS = "Development"

ENABLED_MODULES = [
    "authentication",
    "multiplayer",
    "leaderboard",
    "websocket",
    "ai_bot",
    "matchmaking"
]

def project_info():
    return {
        "name": __project__,
        "version": __version__,
        "status": PROJECT_STATUS
    }

def load_environment():
    print("Loading project environment...")

def initialize_project():
    print("Initializing Ludo Project")

load_environment()
initialize_project()
