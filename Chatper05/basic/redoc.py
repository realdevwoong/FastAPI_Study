from fastapi import FastAPI

app = FastAPI(title="Ex01 - Hello")

# 1. 기본 엔드포인트
@app.get("/")
def root():
    return {"message": "Hello FastAPI"}

# 2. 단순 문자열 리턴
@app.get("/ping")
def ping():
    return {"message": "pong"}

# 3. 경로 파라미터 사용
@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}!"}

# 4. 쿼리 파라미터 사용
@app.get("/add")
def add(x: int, y: int):
    return {"result": x + y}

# 5. 여러 경로 - 고정 값 응답
@app.get("/items")
def get_items():
    return {"items": ["apple", "banana", "cherry"]}

@app.get("/status")
def status():
    return {"status": "ok", "service": "FastAPI running"}