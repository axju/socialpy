import os
import sys
import argparse
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "socialpy.server.settings.data")
try:
    django.setup()
    from socialpy.server.data.models import Post, Category
except ImportError as exc:
    raise ImportError(
        "Couldn't import Django. Are you sure it's installed and "
        "available on your PYTHONPATH environment variable? Did you "
        "forget to activate a virtual environment?"
    ) from exc
