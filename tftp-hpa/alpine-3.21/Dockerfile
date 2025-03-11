# diun.enable=true
# diun.metadata.platforms=linux/amd64,linux/arm64
# diun.metadata.output_image=tftp-hpa
# diun.metadata.output_tag=alpine-3.21
FROM alpine:3.21

RUN apk add --no-cache --update tftp-hpa

ENTRYPOINT [ "in.tftpd" ]
