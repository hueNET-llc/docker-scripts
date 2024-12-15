# diun.enable=true
# diun.metadata.platforms=linux/amd64,linux/arm64
# diun.metadata.output_image=postfix
# diun.metadata.output_tag=alpine-edge
FROM alpine:edge

COPY entrypoint.sh /entrypoint.sh

RUN apk update && \
    apk upgrade && \
    apk add --no-cache postfix postfix-pcre lmdb cyrus-sasl cyrus-sasl-login && \
    chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]