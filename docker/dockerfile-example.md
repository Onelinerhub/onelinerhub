# Dockerfile example

```text
FROM ubuntu:latest
MAINTAINER Oneliner Hub
RUN apt update
RUN apt install nginx
VOLUME "/var/www"
EXPOSE 80
CMD nginx -g "daemon off;"

```

- `FROM ubuntu:latest` - create an image based on ubuntu:latest
- `MAINTAINER` - set author name
- `RUN` - commands to install everything on the image
- `apt install nginx` - install Nginx webserver
- `VOLUME "/var/www"` - share /var/www to the container
- `EXPOSE 80` - make 80 port available from main machine
- `CMD` - command to run within container
- `nginx -g "daemon off;"` - run nginx in foregroung

group: dockerfile

