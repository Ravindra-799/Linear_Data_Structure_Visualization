FROM python:3.9
WORKDIR app
COPY . /Linear_app
EXPOSE 8003
CMD ["python","main.py","runserver","0.0.0.0:8003"]
