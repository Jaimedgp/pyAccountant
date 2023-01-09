import uvicorn

from . import create_api


app = create_api()


if __name__ == '__main__':
    uvicorn.run(app)
