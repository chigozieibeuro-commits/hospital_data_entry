FROM python:3.13

WORKDIR /app

COPY  requirement.text .

RUN pip install --no-cache-dir requirement.text

COPY . .

Expose 8000

CMD ["uvicorn","main:app","--host","0.0.0.0"."--port","8000"]
