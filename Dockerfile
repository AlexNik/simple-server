FROM python:alpine

COPY main.py /main.py

EXPOSE 8000

ENTRYPOINT ["python", "/main.py"]
