FROM python:3.9-alpine

WORKDIR /app

ENV FLASK_RUN_HOST 0.0.0.0

RUN apk add --no-cache gcc musl-dev linux-headers

COPY . /app 

RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "manage.py", "run" ]