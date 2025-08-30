from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Ex04 - POST Body (Model)")

class Item(BaseModel):
    name: str
    price: float

@app.post("/items")
def create_item(item: Item):
    return item

#요청 바디(JSON)를 **Pydantic 모델(Item)**로 검증.

#name은 문자열, price는 숫자가 아니면 자동으로 422 오류 반환.

#입력값 검증 + 문서 자동화가 동시에 이루어짐.