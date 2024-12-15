# diun.enable=true
# diun.metadata.platforms=linux/amd64,linux/arm64
# diun.metadata.output_image=apcupsd
# diun.metadata.output_tag=alpine-3.21
FROM alpine:3.21

RUN apk add --no-cache apcupsd curl mailx msmtp tzdata && \
    ln -sf /usr/bin/msmtp /usr/bin/sendmail && \
    ln -sf /usr/bin/msmtp /usr/sbin/sendmail

COPY mail.rc /etc/mail.rc

CMD [ "apcupsd", "-b" ]