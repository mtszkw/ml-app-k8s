FROM python:3.8

RUN pip install pipenv
COPY Pipfile* /tmp/

RUN cd /tmp && pipenv lock --keep-outdated --requirements > requirements.txt
RUN pip install -r /tmp/requirements.txt

WORKDIR /tmp/myapp/
COPY . .

CMD ["uvicorn", "boston_inference:app", "--host", "0.0.0.0", "--port", "8000"]