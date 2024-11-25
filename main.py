from fastapi import FastAPI, status

app = FastAPI()

@app.get('/',status_code=status.HTTP_200_OK)
async def home():
    return {"message":"This is my first fastapi route"}

