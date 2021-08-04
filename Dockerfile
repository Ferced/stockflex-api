FROM python:3.9

WORKDIR /app
COPY requirements.txt .
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "manage.py", "run" ]