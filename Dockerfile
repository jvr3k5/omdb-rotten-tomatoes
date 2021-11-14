FROM python:3.9.8

ENV WORKDIR=/opt 

WORKDIR $WORKDIR

COPY ./requirements.txt ./

RUN pip3 install -r $WORKDIR/requirements.txt

USER 1001

COPY ./src ./src

ENTRYPOINT ["python3", "-m", "src"]
