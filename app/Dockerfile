FROM python:latest
WORKDIR /app
COPY app.py app.py

RUN groupadd -r appuser && useradd -r -g appuser appuser
RUN chown -R appuser:appuser /app

HEALTHCHECK CMD curl --fail http://localhost:8000/hostname || exit 1

USER appuser

CMD ["python3", "app.py"]
