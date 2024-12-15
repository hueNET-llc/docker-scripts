# diun.enable=true
# diun.metadata.platforms=linux/amd64,linux/arm64
# diun.metadata.output_image=dnsmasq
# diun.metadata.output_tag=alpine-edge
FROM alpine:edge

RUN apk update && \
    apk add --no-cache dnsmasq

USER 100

CMD [ "dnsmasq", "-k", "--user=dnsmasq", "--log-facility=-", "--conf-file=/etc/dnsmasq.conf" ]
