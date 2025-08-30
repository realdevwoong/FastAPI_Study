from fastapi import FastAPI

tags_metadata = [
    {"name": "public", "description": "공개 엔드포인트"},
    {"name": "admin", "description": "관리자 엔드포인트"},
    {"name": "private", "description": "비공개 엔드포인트"}
]

app = FastAPI(
    title="Ex10 - Docs & Tags",
    description="OpenAPI 자동 문서 & 태그 사용 예제",
    version="1.0.0",
    openapi_tags=tags_metadata
)

@app.get("/health", tags=["public"], summary="헬스체크")
def health():
    return {"status": "ok"}

@app.get("/admin/ping", tags=["admin"], summary="관리자 핑")
def admin_ping():
    return {"pong": True}
@app.get("/health", tags=["public"], summary="헬스체크")
def health():
    return {"status": "ok"}

@app.get("/admin/pong", tags=["private"], summary="관리자 핑")
def admin_ping():
    return {"ping": True}