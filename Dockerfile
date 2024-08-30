FROM python:3.11.4-slim-buster as builder

WORKDIR /shop

ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    libcairo2 \
    libgdk-pixbuf2.0-0 \
    libglib2.0-0 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libpangoft2-1.0-0 \
    && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /shop/entrypoint.sh
RUN chmod +x /shop/entrypoint.sh

ENTRYPOINT ["/shop/entrypoint.sh"]

