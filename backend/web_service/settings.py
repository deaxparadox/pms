import os

from .logging import logging

WEB_SETTINGS = os.getenv("WEBSETTINGS", 0)
logging.debug(f"WEBSETTINGS: {WEB_SETTINGS}")
match int(WEB_SETTINGS):
    case 0:
        logging.debug(f"Loading local settings")
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings.local')    
    case 1:
        logging.debug(f"Loading production settings")
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings.production')
    case 2:
        logging.debug(f"Loading docker settings")
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings.docker')



__all__ = ""