FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
RUN pip install pandas
EXPOSE 80
COPY ./app /app
