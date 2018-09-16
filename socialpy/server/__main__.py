#!/usr/bin/env python
import os
import sys
import argparse
import django

def main():
    parser = argparse.ArgumentParser(description='SocialPy | SERVER')
    parser.add_argument('action', type=str, choices=['run', 'setup', 'deletedb', 'createadmin'])
    parser.add_argument('--settings', type=str, choices=['server', 'local', 'development'], default='local')

    args = parser.parse_args()

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "socialpy.server.settings."+args.settings)
    try:
        django.setup()
        from django.conf import settings
        from django.core.management import call_command
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    if args.action == 'run':
        if args.settings in ['local', 'development']:
            call_command('runserver', '--insecure')
        else:
            call_command('runserver',  '0.0.0.0:9999', '--insecure')

    elif args.action == 'setup':
        try:
            os.makedirs(settings.MEDIA_ROOT)
        except Exception as e:
            pass
        call_command('migrate', '--noinput')
        call_command('collectstatic', '--noinput')

    elif args.action == 'deletedb':
        file = settings.DATABASES['default']['NAME']
        os.remove(file)
        print('delete database:', file)

    elif args.action == 'createadmin':
        call_command('createsuperuser')

if __name__ == "__main__":
    main()
