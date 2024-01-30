from dotenv import dotenv_values
import os


print("\nLoading ENVs\n")
config = dotenv_values(".env.dev")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}

os.environ.setdefault("DJANGO_ALLOW_ASYNC_UNSAFE", "1")