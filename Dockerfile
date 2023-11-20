FROM python:3.8-alpine as packages

RUN apk add g++ libc-dev libffi-dev
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

COPY requirements.txt ./

ENV PIP_USER=1
ENV PIP_IGNORE_INSTALLED=1
ENV PYROOT /pyroot
ENV PYTHONUSERBASE $PYROOT

RUN pip install -r requirements.txt
RUN pip install python-telegram-bot -U --pre

# Build
FROM python:3.8-alpine

ENV PYTHONUNBUFFERED=1
ENV TZ=Africa/Johannesburg

RUN apk add tzdata

WORKDIR /mnt/unite180

COPY --from=packages /pyroot/ /usr/local/

COPY . .

EXPOSE 8080

CMD ["python", "unite180_service.py"]
