from fastapi import FastAPI, Request
from fastapi.responses import Response

app = FastAPI()

@app.get("/set_cookie")
def set_cookie():
    response = Response(content="쿠키 설정 완료")
    # 20초 동안 유지되는 쿠키 설정 (Flask의 max_age와 동일)
    response.set_cookie(key="username", value="woong", max_age=20)
    return response

@app.get("/get_cookie")
def get_cookie(request: Request):
    username = request.cookies.get("username")
    return {"쿠키 값": username}
