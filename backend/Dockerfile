FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /var/www/apps/employee-crm/backend

COPY requirements.txt /var/www/apps/employee-crm/backend

RUN pip install -r requirements.txt

COPY . /var/www/apps/employee-crm/backend
