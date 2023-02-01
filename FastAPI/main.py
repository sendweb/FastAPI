from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/')
async def index():
    return 'ok'


@app.get('/test2')
async def test2():
    return {"message": "Hello World"}

@app.post('/test2')
async def test2():
    return {"message": "Hello World ,this is post method"}

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True, host="localhost", port=8080)
