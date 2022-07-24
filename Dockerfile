FROM python:3.8

ENV PYTHONUNBUFFERED=1 TIMEZONE=UTC+2
RUN apt-get update

RUN mkdir -p /usr/src/app/
ARG WORKDIR=/usr/src/app/

WORKDIR ${WORKDIR}

RUN python -m pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install --requirement requirements.txt
COPY . /usr/src/app/

ARG USER=user
ARG UID=1000

#Добавляем нового юзера с идентификатором
RUN useradd --system ${USER} --uid=${UID}
#Меняем рекурсивно (на каждую вложенную папку) права,
# точнее владельца всех папок \
RUN chown --recursive ${USER} ${WORKDIR}

#Декларируем порт, что бы потом его пробросить:
EXPOSE 8000

#Укажем переменную окружения:
#ENV UTC+2

#Переменные окружения используются напр.:
# Указать путь к какому то файлу, ID-клиентов,
#URL

# Переменную окружения так же можно указать при сборке контейнера:
#docker run -p 8080:8080 -e TZ Europe/Kiev имя

CMD python3 manage.py makemigrations; python3 manage.py migrate; python3 manage.py runserver 0.0.0.0:8000
