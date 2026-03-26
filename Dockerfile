#FastAPI 서버 컨테이너 만드는 방법 정의
FROM python:3.10

WORKDIR /app

COPY ./app /app

RUN pip install fastapi uvicorn

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

