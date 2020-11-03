"""
WSGI config for msm_dgdjh_67_dev_14484 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'msm_dgdjh_67_dev_14484.settings')

application = get_wsgi_application()
