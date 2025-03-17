# Python 3.9 slim 이미지 사용
FROM python:3.9-slim

# 작업 디렉토리 설정
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt


COPY . /app/
# 필요한 파일 복사
COPY templates /app/templates 

# FastAPI 및 Uvicorn 설치
EXPOSE 8000
# FastAPI 실행
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
