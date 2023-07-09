FROM python:3.11.4

ENV PYTHONUNBUFFERED 1
ENV PROJECT_DIR /project/app

WORKDIR $PROJECT_DIR

ADD requirements.txt $PROJECT_DIR/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . $PROJECT_DIR
