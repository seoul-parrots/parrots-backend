FROM python:3.8-alpine

WORKDIR /app

# 필요한 dependency 를 설치합니다.
COPY requirements.txt .
RUN pip3 install --no-cache-dir --upgrade pip
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

ADD parrots_backend

ENTRYPOINT ["uvicorn", "parrots_backend.app:app"]

EXPOSE 8080
CMD ["--host", "0.0.0.0", "--port", "8080"]
