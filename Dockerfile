FROM python:3.10-slim-buster
COPY model /model
COPY requirements.txt /requirements.txt
COPY api /api
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD uvicorn api.api:app --host 0.0.0.0 --port $PORT
