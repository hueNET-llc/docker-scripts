# tftp-hpa:alpine-3.21
[![GitHub](https://img.shields.io/badge/GitHub-blue)](https://github.com/hueNET-llc/docker-scripts/tree/master/tftp-hpa) [![Docker Hub Image](https://img.shields.io/docker/v/rafaelwastaken/tftp-hpa/alpine-3.21)](https://hub.docker.com/repository/docker/rafaelwastaken/tftp-hpa)

Alpine-based tftp-hpa server

Args are passed directly to `in.tftpd`. There are no args passed by default.

Example usage:
```
docker run rafaelwastaken/tftp-hpa:alpine-3.21 --foreground --secure /tftp
```