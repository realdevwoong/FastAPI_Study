import os
from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from starlette.middleware.sessions import SessionMiddleware

# 환경변수나 랜덤 키 사용 가능
SECRET_KEY = os.urandom(24)  
# SECRET_KEY = os.getenv("SECRET_KEY", os.urandom(24))

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)


@app.get("/set_session")
async def set_session(request: Request):
    request.session["username"] = "woong"
    return PlainTextResponse("세션 설정 완료")


@app.get("/get_session")
async def get_session(request: Request):
    username = request.session.get("username")
    return PlainTextResponse(f"세션 값: {username}")