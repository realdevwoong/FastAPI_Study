#경로 파라미터
from fastapi import FastAPI

app = FastAPI(title="Example 1: Routing & Docs")

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}