FROM python:latest

WORKDIR /homeapi
COPY requirements.txt /homeapi/requirements.txt
RUN pip install -r requirements.txt

COPY ./app /homeapi/app

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]