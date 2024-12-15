# diun.enable=true
# diun.metadata.platforms=linux/amd64,linux/arm64
FROM alpine:edge

COPY entrypoint.sh /entrypoint.sh

RUN apk update && \
    apk upgrade && \
    apk add --no-cache postfix postfix-pcre lmdb cyrus-sasl cyrus-sasl-login && \
    chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]