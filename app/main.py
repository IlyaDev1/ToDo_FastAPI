import uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get('/', summary='Главная ручка')
def root():
    return {'msg': 'start'}


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True, port=8080)
