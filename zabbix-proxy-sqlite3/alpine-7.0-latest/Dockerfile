# diun.enable=true
# diun.metadata.platforms=linux/amd64,linux/arm64
FROM zabbix/zabbix-proxy-sqlite3:alpine-7.0-latest

USER root

RUN apk update && \
    apk add --no-cache jq expect openssh sshpass tini

ENTRYPOINT ["/sbin/tini", "--", "/usr/bin/docker-entrypoint.sh"]

USER 1997

CMD ["/usr/sbin/zabbix_proxy", "--foreground", "-c", "/etc/zabbix/zabbix_proxy.conf"]