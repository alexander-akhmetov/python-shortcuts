FROM python:3.11.1-slim

RUN pip install python-shortcuts==0.11.0

ENTRYPOINT ["shortcuts"]
