# Python 이미지
FROM python:3.12-slim

# 작업 디렉토리
WORKDIR /app

# 파일 복사
COPY . .

# 패키지 설치
RUN pip install --no-cache-dir -r requirements.txt

# Flask 실행 환경 변수
ENV FLASK_APP=app.main
ENV FLASK_RUN_HOST=0.0.0.0

# 포트
EXPOSE 5000

# 실행
CMD ["flask", "run"]

