from .base import *

from bserver.config import config

SECRET_KEY = config.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config.get("DEBUG")

ALLOWED_HOSTS = config.get("ALLOWED_HOSTS").split(" ")

print("\n############ Starting the LOCAL SERVER ############\n")