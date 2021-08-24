FROM python:3.8

ENV PYTHONUNBUFFERED 1
RUN apt-get update \
    && apt-get install -y vim \
    && apt-get install -y --no-install-recommends
RUN mkdir /code
WORKDIR /code 
ADD requirements.txt /code/ 
RUN pip install --upgrade pip \
    && pip install -r requirements.txt 
ADD . /code/ 

EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

# FROM python:3.6

# RUN apt-get update \
#     && apt-get install -y --no-install-recommends \
#         postgresql-client \
#     && rm -rf /var/lib/apt/lists/*

# RUN apt-get update \ 
#   && apt-get install -y --no-install-recommends openssh-server \
#   && echo "root:Docker!" | chpasswd

# RUN mkdir /app
# WORKDIR /app
# ADD . /app/
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# # WORKDIR /usr/src/app
# # COPY requirements.txt ./
# RUN pip install -r requirements.txt
# # RUN python manage.py collectstatic
# # COPY . /app/

# EXPOSE 8000
# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]