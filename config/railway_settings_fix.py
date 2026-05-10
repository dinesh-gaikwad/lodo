import os

ALLOWED_HOSTS = ["*"]

DEBUG = False

CSRF_TRUSTED_ORIGINS = [
    "https://*.railway.app",
    "https://*.up.railway.app"
]

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
