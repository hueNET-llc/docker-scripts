# diun.enable=true
# diun.metadata.platforms=linux/amd64,linux/arm64
FROM zabbix/zabbix-server-pgsql:trunk-alpine

USER root

RUN apk update && \
    apk add --no-cache jq expect openssh sshpass tini

ENTRYPOINT ["/sbin/tini", "--", "/usr/bin/docker-entrypoint.sh"]

USER 1997

CMD ["/usr/sbin/zabbix_server", "--foreground", "-c", "/etc/zabbix/zabbix_server.conf"]