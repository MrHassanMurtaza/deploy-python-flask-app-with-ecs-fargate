# Base image
FROM python:alpine

# Creating work directory in docker
WORKDIR /usr/app

# Copying files to docker
ADD . '/usr/app'

# Installing Flask App
RUN pip install flask

# Exposing the flask app port from container to host
EXPOSE 5000

# Starting application
CMD ["python", "app.py"]
