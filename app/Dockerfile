FROM python:3.7.5-buster
RUN apt-get update
RUN apt-get install uwsgi-plugin-python3 -y
COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt
COPY . /
ENV HOME /app
WORKDIR /app
RUN chmod +x ./app.ini
EXPOSE 5000
RUN pytest
CMD ["uwsgi" ,"--ini" ,"./app.ini"]