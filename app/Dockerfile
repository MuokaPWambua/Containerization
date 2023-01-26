FROM python:3.8.10-alpine

ENV PATH="$PATH:/home/app/.local/bin"
RUN apk update \
    && apk add netcat-openbsd \
    && apk add --virtual py3-pip build-base \
    && apk add --virtual python3-dev gcc libc-dev linux-headers pcre-dev
# Copy the current directory contents into the container at /app 
COPY . /app
RUN chmod +x /app/entrypoint.sh
# create the app user without password and permit root access
RUN adduser -D app
RUN echo 'permit app as root' > /etc/doas.conf
# change app user to app
USER app
WORKDIR /app
RUN ls -al
# Install app requirements
RUN pip install --upgrade pip \
    && pip3 install -r requirements.txt
