FROM python:3.9
WORKDIR app
COPY . /Linear_app
RUN pip install -r requirements.txt 
EXPOSE 8001
CMD ["python","main.py","runserver","0.0.0.0:8001"]
