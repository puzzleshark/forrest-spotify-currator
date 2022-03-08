ARG BUILD_FROM
FROM $BUILD_FROM


#RUN apt-get update
#RUN apt-get install ffmpeg -y

RUN wget http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-armv7l.sh

RUN /bin/bash Miniconda3-latest-Linux-armv7l.sh -b -p /opt/conda

ENV PATH=/opt/conda:$PATH

COPY requirements.txt /usr/src/requirements.txt
RUN pip install -r /usr/src/requirements.txt

COPY src /usr/src
WORKDIR /usr/src

CMD python currate.py

