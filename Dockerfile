FROM python:3.12
ADD . /auth
WORKDIR /auth
RUN pip install -r requirements.txt
CMD ["python", "server.py"]