FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /dm_rest
COPY ./requirements.txt /dm_rest
RUN pip install -r /dm_rest/requirements.txt
COPY . /dm_rest
EXPOSE 8000
