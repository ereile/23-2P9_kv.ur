"""api для решение уравнения"""
from fastapi import FastAPI
from main import kv_ur
app = FastAPI()


@app.get("/get_answer/")
async def get_answer(a: float, b: float, c: float):
    """Получения ответа"""
    output = kv_ur(a, b, c)
    return output
