#실제 API 서버 프로그램
#사용자 요청 받음, 응답 반환, DB연결
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello Docker + MariaDB 🚀"}

