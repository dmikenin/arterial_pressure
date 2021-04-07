import uvicorn
from fastapi import FastAPI

from api.v1 import routes


app = FastAPI(title='Arterial Pressue Documentation',
              description='Documentation for backend AP',
              version='0.0.1')


app.include_router(routes.router, prefix="/api")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8022)