# Python 3.9 slim 이미지 사용
FROM python:3.9-slim

# 작업 디렉토리 설정
WORKDIR /app

# requirements.txt 복사
COPY requirements.txt /app/
# 패키지 설치
RUN pip install --no-cache-dir -r requirements.txt

# 앱 파일 복사
COPY . /app/
# COPY server2/main.py /app/main.py

# 포트 노출
EXPOSE 8001

# FastAPI 실행
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
