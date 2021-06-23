FROM python:3

RUN pip install flask

COPY . /app
CMD [ "python", "./app/app.py" ]
