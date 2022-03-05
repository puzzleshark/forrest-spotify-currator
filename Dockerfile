ARG BUILD_FROM
FROM $BUILD_FROM


#RUN apt-get update
#RUN apt-get install ffmpeg -y

COPY requirements.txt /usr/src/requirements.txt
RUN pip install -r /usr/src/requirements.txt

COPY src /usr/src
WORKDIR /usr/src

CMD python entry.py

