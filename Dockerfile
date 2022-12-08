FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
RUN pip install pandas
RUN pip install requests
EXPOSE 80
COPY ./app /app
