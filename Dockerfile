FROM python:3.10-buster
ENV AM_I_IN_A_DOCKER_CONTAINER Yes

# Installing Oracle instant client
WORKDIR    /opt/oracle
RUN        apt-get update && apt-get install -y libaio1 wget unzip \
            && wget https://download.oracle.com/otn_software/linux/instantclient/instantclient-basiclite-linuxx64.zip \
            && unzip instantclient-basiclite-linuxx64.zip \
            && rm -f instantclient-basiclite-linuxx64.zip \
            && cd /opt/oracle/instantclient* \
            && rm -f *jdbc* *occi* *mysql* *README *jar uidrvci genezi adrci \
            && echo /opt/oracle/instantclient* > /etc/ld.so.conf.d/oracle-instantclient.conf \
            && ldconfig

RUN pip install --upgrade pip && \
    pip install pipenv==2022.10.4

COPY . /app
WORKDIR /app

RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy

EXPOSE 8080
EXPOSE 8081
EXPOSE 1521
CMD pipenv run python manage.py runserver 0.0.0.0:8081