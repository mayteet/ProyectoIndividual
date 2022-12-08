FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
RUN pip install -r requeriments.txt
EXPOSE 80
COPY ./app /app
