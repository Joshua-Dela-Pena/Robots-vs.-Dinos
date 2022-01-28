FROM node:alpine

WORKDIR /user/app

COPY requirements.txt/ ./
RUN pip install

USER appuser

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1


CMD ["python", "main.py"]