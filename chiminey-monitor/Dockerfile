FROM        phusion/baseimage:0.9.16

MAINTAINER  Ian Thomas <ianedwardthomas@gmail.com>

RUN apt-get -y update && apt-get -y install python-dev python-pip

RUN pip install https://github.com/mher/flower/zipball/0.9 redis

EXPOSE 5555

ENTRYPOINT ["flower", "--port=5555"]

