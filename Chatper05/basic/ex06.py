from fastapi import FastAPI

app = FastAPI(title="Ex06 - Status Code")

@app.post("/created", status_code=202)
def created():
    return {"status": "created"}

#기본 응답코드(200 OK) 대신, 201 Created로 지정 가능.
#REST API에서 자원 생성 시 권장되는 방식.