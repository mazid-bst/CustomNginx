FROM nginx:1.16-alpine

RUN apk update
RUN apk add --no-cache --virtual .build-deps g++ python3-dev libffi-dev openssl-dev && \
    pip3 install --upgrade pip setuptools && \
    apk del .build-deps
RUN apk add --no-cache --update python3
ADD ./index.py  /usr/share/nginx/html/
RUN /usr/bin/python3 /usr/share/nginx/html/index.py
