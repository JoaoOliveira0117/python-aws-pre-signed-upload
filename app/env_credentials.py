from dotenv import dotenv_values

env = dotenv_values(".env")

class DevelopmentConfig():
    DEBUG = True
    MONGODB_SETTINGS = {
        "db": env.get("MONGODB_DATABASE"),
        "host": env.get("MONGODB_HOST")
    }