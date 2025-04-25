from fastapi import FastAPI, Request
from routing.router import route_message

app = FastAPI()

@app.post("/process/")
async def process_request(request: Request):
    data = await request.json()
    result = await route_message(data)
    return result