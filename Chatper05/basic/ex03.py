from fastapi import FastAPI, Query

app = FastAPI(title="Ex03 - Query Params")

@app.get("/search")
def search(q: str | None = Query(default=None, description="검색어")):
    return {"query": q}

#http://localhost:8000/search?q=python
#/search?q=python → 쿼리스트링 파라미터 q 값을 받음.
#타입 힌트(str | None)로 문자열/없음을 구분.
#description="검색어"는 문서(/docs)에 자동 반영.