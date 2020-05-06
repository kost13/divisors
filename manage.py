#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def add_divisors_to_path():    
    bin_path = os.path.dirname(os.path.abspath(__file__)) + "/bin"
    if not bin_path in sys.path:
        sys.path.append(bin_path)


def main():
    add_divisors_to_path()
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'divisors_site.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
