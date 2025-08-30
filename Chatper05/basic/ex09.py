from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI(title="Ex09 - Custom Response")

@app.get("/plain", response_class=PlainTextResponse)
def plain():
    return "text/plain 응답입니다."

#기본은 JSON 응답이지만, response_class로 다른 타입 가능.
#여기서는 text/plain 문자열 응답을 반환.