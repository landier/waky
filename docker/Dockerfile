FROM python:3.7
LABEL maintainer="nicolas.landier@gmail.com"

RUN DEBIAN_FRONTEND=noninteractive \
    apt update && \
    apt install -y vim

RUN pip install --upgrade pip

ADD . /app
WORKDIR /app
RUN pip install .

CMD ["/usr/local/bin/waky"]
