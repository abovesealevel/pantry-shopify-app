FROM node:latest AS build
ARG API_URL_FOR_SHOPIFY
ENV API_URL_FOR_SHOPIFY=${API_URL_FOR_SHOPIFY}

FROM python:3.9.0-slim-buster AS production
#WORKDIR /app
COPY requirements.txt requirements.txt  
RUN python3 -m pip install -r requirements.txt --no-cache-dir
COPY . .
COPY /app_shopify/templates/*.html /app_shopify/templates/static/
COPY /app_shopify/templates/static/ /app_shopify/templates/static/
ENV PORT 5000

CMD gunicorn wsgi:app --preload -b :$PORT --timeout 120 --workers 5 --keep-alive 60 --log-level=debug

#RUN chmod +x /docker-entrypoint.sh
#ENTRYPOINT ["./docker-entrypoint.sh"]
