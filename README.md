# Flask-Docker-App

A very simple application to to learn how to dockerize a flask application

Creating the flask application is very eay and can be found on the internet

## Usefull link [here](https://docs.docker.com/language/python/build-images/).

### Usefull Commands

- docker build --tag python-docker .
  to create docker images
- docker run -it -d -p 5000:5000 python-docker
  to run the containrized application
- docker images
  to check docker images
- docker rmi python-docker
  to remove docker image
