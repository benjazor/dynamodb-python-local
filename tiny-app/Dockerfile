FROM python:3.9.4-alpine3.12
WORKDIR /tiny-app
ADD . /tiny-app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]