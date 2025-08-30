from fastapi import FastAPI, Depends, HTTPException, Security, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

app = FastAPI(title="Ex08 - Depends(Auth) • HTTPBearer (Swagger Authorize)")

# Swagger에 securitySchemes가 자동 등록되고, 우상단 Authorize 버튼이 활성화됨
bearer_scheme = HTTPBearer(auto_error=False)

def get_bearer_token(
    credentials: HTTPAuthorizationCredentials | None = Security(bearer_scheme)
) -> str:
    # 1) 헤더가 아예 없는 경우
    if credentials is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing Bearer token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # 2) 스킴 검증 (기본적으로 "bearer" 소문자로 들어옴)
    if credentials.scheme.lower() != "bearer":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authorization scheme",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # 3) 토큰 추출
    token = credentials.credentials.strip()
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Empty token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return token

@app.get("/me")
def me(token: str = Depends(get_bearer_token)):
    return {"ok": True, "token_preview": token[:6] + "..."}