# Base Image
FROM python:3.7

# create and set working directory
WORKDIR /blog_portfolio

# set default environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1


COPY Pipfile Pipfile.lock /blog_portfolio/
RUN pip install --upgrade pip
RUN pip install pipenv && pipenv install --system

COPY requirements.txt /blog_portfolio/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /blog_portfolio/
