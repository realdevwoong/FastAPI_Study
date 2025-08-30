from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Ex05 - response_model")

class ItemIn(BaseModel):
    name: str
    price: float
    secret: str | None = Field(default=None, description="응답에서 숨길 필드")

class ItemOut(BaseModel):
    name: str
    price: float

@app.post("/items", response_model=ItemOut)
def create_item(item: ItemIn):
    return item

#ItemIn은 요청 바디, ItemOut은 응답 스키마.#
#요청 시 secret을 보낼 수 있지만, 응답에는 표시되지 않음.
#response_model → 출력 필드를 통제할 수 있음.