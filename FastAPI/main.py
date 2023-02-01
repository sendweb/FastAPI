from fastapi import FastAPI
import uvicorn
import json

app = FastAPI()

data = {'key1': 'value1', 'key2': 'value2'}

@app.get('/')
async def index():
    return 'ok'


@app.get('/test1')
async def test1():
    return {"message": "Hello World"}

@app.post('/test2')
async def test2():
    return {"message": "Hello World ,This is post method. It work/r来点中文看看."}

@app.post('/test3')
async def test3():
    print(data)
    return data

@app.post('/test4')
async def test4():
    # 我们用到了json库的dumps方法，将Python对象转化为Json对象
    json_data = json.dumps(data)
    print(json_data)
    return json_data

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True, host="localhost", port=8080)
