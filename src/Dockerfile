FROM python:3.9-slim

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ./requirements.txt /tmp/requirements.txt
RUN pip install \
    --no-cache-dir \
    -r /tmp/requirements.txt

# set working directory
WORKDIR /code
# copy project
COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]