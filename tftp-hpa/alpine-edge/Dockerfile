# diun.enable=true
# diun.metadata.platforms=linux/amd64,linux/arm64
# diun.metadata.output_image=tftp-hpa
# diun.metadata.output_tag=alpine-edge
FROM alpine:edge

RUN apk add --no-cache --update tftp-hpa tzdata

ENTRYPOINT [ "in.tftpd" ]
