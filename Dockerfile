FROM python:3

RUN mkdir /summation
WORKDIR /summation
COPY requirements.txt /summation/
RUN pip install -r requirements.txt
COPY . /summation/

EXPOSE 8000
CMD python manage.py runserver 127.0.0.1:8000
