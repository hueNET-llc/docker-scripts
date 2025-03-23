# diun.enable=true
# diun.metadata.platforms=linux/amd64,linux/arm64
# diun.metadata.output_image=zabbix-server-pgsql
# diun.metadata.output_tag=alpine-7.2-latest
FROM zabbix/zabbix-server-pgsql:alpine-7.2-latest

USER root

RUN apk add --update --no-cache jq expect openssh sshpass tini

ENTRYPOINT ["/sbin/tini", "--", "/usr/bin/docker-entrypoint.sh"]

USER 1997

CMD ["/usr/sbin/zabbix_server", "--foreground", "-c", "/etc/zabbix/zabbix_server.conf"]