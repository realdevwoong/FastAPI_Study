from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/set_cookie")
async def set_cookie():
    response = PlainTextResponse("쿠키 설정 완료")
    # max_age는 초 단위 → 20초 유지 (Flask 코드와 동일)
    response.set_cookie(key="username", value="woong", max_age=20)
    return response


@app.get("/get_cookie")
async def get_cookie(request: Request):
    username = request.cookies.get("username")
    return PlainTextResponse(f"쿠키 값: {username}")