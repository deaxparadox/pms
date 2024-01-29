from dotenv import dotenv_values


print("\nLoading ENVs\n")
config = dotenv_values(".env.dev")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}

