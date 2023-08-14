FROM python:3.11.3-alpine3.17

WORKDIR /app

RUN apk update && apk add --no-cache \
    build-base \
    git \
    inotify-tools \
    openssh-client

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir /root/.ssh
RUN ssh-keyscan github.com >> /root/.ssh/known_hosts

EXPOSE 8000

CMD ["sh", "start.sh"]