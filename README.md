# CS599 Presentation - Containerization with Docker

Hello-world of docker:

```docker run hello-world```

Building a custom image from a dockerfile:

```docker build -t jonasmh/cs599:latest ./example_app```

Publish to the hub:

```docker push jonasmh/cs599```

Now everyone is able to pull your image and use it!

## docker-compose ##

Docker-compose helps you manage multiple containers. This is done by writing down what containers you need in a docker-compose.yml file. After the docker-compose.yml is written the following command is used to start:

```docker-compose up```

The flag `-d` can be added to the command to start without connecting the terminal to the output.

When ready to shut down simply use

```docker-compose down```