from fastapi import FastAPI

app = FastAPI(title="내 FastAPI 예제", description="자동 문서화 연습", version="1.0.0")

@app.get("/hello")
def hello(name: str = "World"):
    """
    간단한 Hello API

    - **name**: 이름을 입력하면 "Hello {name}" 반환
    """
    return {"message": f"Hello {name}"}