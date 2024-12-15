# diun.enable=true
# diun.metadata.platforms=linux/amd64,linux/arm64
FROM crazymax/diun:latest

RUN apk update && \
    apk add --no-cache python3 py3-pip docker docker-cli-buildx && \
    pip3 install --no-cache-dir --break-system-packages requests
    