FROM python:3.10.0

COPY . /home/main
WORKDIR /home/main/fashion-recommand-mall

RUN python3 -m pip install -U pip
RUN pip3 install -r resource/requirements.txt

RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

CMD gunicorn -c gunicorn.config.py -b 0.0.0.0:8000