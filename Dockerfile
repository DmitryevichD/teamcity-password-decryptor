FROM python:2.7

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT python decrypt.py "$@"
