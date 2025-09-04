import os
from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from starlette.middleware.sessions import SessionMiddleware
# from dotenv import load_dotenv
# load_dotenv()

app = FastAPI()

# Flask의 app.secret_key와 동일한 역할
app.add_middleware(SessionMiddleware, secret_key=os.urandom(24))
# app.add_middleware(SessionMiddleware, secret_key=os.getenv("SECRET_KEY"))

@app.get("/set_session")
def set_session(request: Request):
    request.session["username"] = "woong"
    return PlainTextResponse("세션 설정 완료")

@app.get("/get_session")
def get_session(request: Request):
    username = request.session.get("username")
    return PlainTextResponse(f"세션 값: {username}")