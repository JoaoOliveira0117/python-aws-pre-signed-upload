from dotenv import dotenv_values
from app.config import create_app

env = dotenv_values(".env")
app = create_app()

if __name__ == '__main__':
    app.run(host=env.get("APP_HOST"), port=env.get("APP_PORT"))