FROM python:3
ADD app/ /app
WORKDIR /app
RUN apt-get update
RUN pip install -r requirements.txt
RUN nosetests tests/test_sum_mul.py --with-coverage --cover-package=app
CMD python app.py