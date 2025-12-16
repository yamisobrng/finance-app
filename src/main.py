from fastapi import FastAPI

app = FastAPI(
    title='Finance App',
    description='API для учета личных финансов. Стек: FastAPI, SQLAlchemy, Docker.',
    version = '1.0.0'
)

@app.get('/ping')
async def pong():
    return {'message': 'pong', 'status': 'ok'}