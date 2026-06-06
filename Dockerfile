FROM python:3.13-bookworm

ENV DEBIAN_FRONTEND=noninteractive

ENV PATH="/usr/local/bin:${PATH}" \
    PYTHONUNBUFFERED=1

WORKDIR /

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        curl \
        nginx \
        supervisor \
        ca-certificates \
        tar \
    && rm -rf /var/lib/apt/lists/*


# For ARM64 (Apple M1/M2/M3, AWS Graviton)
RUN curl -L "https://temporal.download/cli/archive/latest?platform=linux&arch=arm64" \
    -o /tmp/temporal.tar.gz \
    && tar -xzf /tmp/temporal.tar.gz -C /usr/local/bin temporal \
    && rm /tmp/temporal.tar.gz \
    && temporal --version

# RUN curl -L "https://temporal.download/cli/archive/latest?platform=linux&arch=amd64" \
#     -o /tmp/temporal.tar.gz \
#     && tar -xzf /tmp/temporal.tar.gz -C /usr/local/bin/ temporal \
#     && rm /tmp/temporal.tar.gz \
#     && temporal --version

COPY pyproject.toml  .
RUN python -m pip install --no-cache-dir uv \
    && uv sync

COPY . .
RUN mkdir -p /var/log/supervisor /var/log/nginx
RUN rm -f /etc/nginx/sites-enabled/default || true

COPY config/nginx.conf /etc/nginx/nginx.conf
COPY config/supervisord.conf /etc/supervisor/supervisord.conf

EXPOSE 80

CMD ["supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf"]
