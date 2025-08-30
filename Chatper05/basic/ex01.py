from fastapi import FastAPI

app = FastAPI(title="Ex01 - Hello")

@app.get("/")
def root():
    return {"message": "Hello FastAPI"}


#@app.get("/") → **루트 경로("/")**에 GET 요청이 오면 실행.
#Python dict를 반환하면 → FastAPI가 자동으로 JSON 응답으로 변환.
#가장 기본적인 FastAPI 서버 구조.