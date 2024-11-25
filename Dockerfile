FROM python:3.8-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY serve_model.py .
COPY model.joblib .
EXPOSE 5000
ENTRYPOINT ["python", "serve_model.py"]
