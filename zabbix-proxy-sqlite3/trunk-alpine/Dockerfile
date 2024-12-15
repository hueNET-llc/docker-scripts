# diun.enable=true
# diun.metadata.platforms=linux/amd64,linux/arm64
# diun.metadata.output_image=zabbix-proxy-sqlite3
# diun.metadata.output_tag=trunk-alpine
FROM zabbix/zabbix-proxy-sqlite3:trunk-alpine

USER root

RUN apk update && \
    apk add --no-cache jq expect openssh sshpass tini

ENTRYPOINT ["/sbin/tini", "--", "/usr/bin/docker-entrypoint.sh"]

USER 1997

CMD ["/usr/sbin/zabbix_proxy", "--foreground", "-c", "/etc/zabbix/zabbix_proxy.conf"]