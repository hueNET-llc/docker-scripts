# tftp-hpa:alpine-edge
[![Docker Hub Image](https://img.shields.io/docker/v/rafaelwastaken/tftp-hpa/alpine-edge)](https://hub.docker.com/repository/docker/rafaelwastaken/tftp-hpa)

Alpine-based tftp-hpa server

Args are passed directly to `in.tftpd`. There are no args passed by default.

Example usage:
```
docker run rafaelwastaken/tftp-hpa:alpine-edge --foreground --secure /tftp
```