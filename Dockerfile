FROM python:3.9.9-slim-bullseye

EXPOSE 80
EXPOSE 8089

ADD requirements.txt ./requirements.txt
RUN pip install -r requirements.txt -U

ADD . ./

ENTRYPOINT [ "bash" ]