FROM python:3.7-alpine3.8

RUN pip install python-shortcuts==0.10.0

ENTRYPOINT ["shortcuts"]
