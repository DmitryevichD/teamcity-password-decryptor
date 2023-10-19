FROM python:2.7-alpine3.11

RUN apk add --no-cache gcc g++ make libffi-dev openssl-dev

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT python decrypt.py "$@"
