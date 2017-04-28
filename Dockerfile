
FROM python:latest

MAINTAINER  Pranjal_Jain

ARG user=app
ARG group=app
ARG uid=2101
ARG gid=2101

RUN \
  apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10 && \
  echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' > /etc/apt/sources.list.d/mongodb.list && \
  apt-get update && \
  apt-get install -y mongodb-org && \
  rm -rf /var/lib/apt/lists/*
VOLUME ["/data/db"]
WORKDIR /data

CMD ["mongod"]

# Expose ports.
#   - 27017: process
#   - 28017: http
EXPOSE 27017
EXPOSE 28017


# The luigi app is run with user `app`, uid = 2101
# If you bind mount a volume from the host or a data container,
# ensure you use the same uid
RUN groupadd -g ${gid} ${group} \
    && useradd -u ${uid} -g ${group} -m -s /bin/bash ${user}

RUN mkdir /etc/luigi
ADD ./etc/luigi/logging.cfg /etc/luigi/
ADD ./etc/luigi/client.cfg /etc/luigi/
VOLUME /etc/luigi

RUN mkdir -p /luigi/tasks
RUN mkdir -p /luigi/tasks/Data
RUN mkdir -p /luigi/work
RUN mkdir -p /luigi/outputs

ADD ./luigi/tasks/ /luigi/tasks

RUN chown -R ${user}:${group} /luigi

VOLUME /luigi/work
VOLUME /luigi/tasks
VOLUME /luigi/outputs

RUN apt-get update && apt-get install -y \
    libpq-dev \
    freetds-dev \
    build-essential



USER ${user}

RUN bash -c "pyvenv /luigi/.pyenv \
    && source /luigi/.pyenv/bin/activate \
    && pip install cython \
    && pip install boto3 boto sqlalchemy luigi pymssql psycopg2 alembic numpy pandas sklearn scipy mechanicalsoup seaborn"

ADD ./luigi/taskrunner.sh /luigi/

ENTRYPOINT ["bash", "/luigi/taskrunner.sh"]
