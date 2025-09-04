from fastapi import FastAPI
import asyncio

app = FastAPI(title="Ex07 - Async")

@app.get("/slow")
async def slow():
    await asyncio.sleep(30)  # I/O 대기 시뮬레이션
    return {"done": True}

#async def 함수 사용 → 비동기 처리 가능.
#Flask와 달리 FastAPI는 ASGI 기반이므로 실제로 동시성 성능을 발휘.
#10초 대기하는 동안에 다른 요청은 정상처리한다는 것 
