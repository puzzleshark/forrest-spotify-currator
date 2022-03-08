ARG BUILD_FROM
FROM $BUILD_FROM


#RUN apt-get update
#RUN apt-get install ffmpeg -y

# RUN wget http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-armvhf.sh
RUN wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-aarch64.sh


ENV CONDA_DIR /opt/conda
# RUN chmod +x Miniforge3-Linux-aarch64.sh
# RUN ./Miniforge3-Linux-aarch64.sh -b -p /opt/conda
RUN /bin/bash ./Miniforge3-Linux-aarch64.sh -b -p /opt/conda

ENV PATH=$CONDA_DIR/bin:$PATH

COPY requirements.txt /usr/src/requirements.txt
RUN pip install -r /usr/src/requirements.txt

COPY src /usr/src
WORKDIR /usr/src

CMD python entry.py

