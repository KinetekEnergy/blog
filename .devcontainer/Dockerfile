FROM ubuntu:latest
WORKDIR /app
ADD . /app
RUN set -xe \
    && apt-get update \
    && apt-get install python3-pip
    && pip install nbconvert
    && python -m pip install nbconvert
    && pip install pyyaml
    && python -m pip install pyyaml
    && pip install enlighten
    && python -m pip install enlighten
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
libstdc++.so.6.0.33
