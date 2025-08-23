# diun.enable=true
# diun.metadata.platforms=linux/amd64,linux/arm64
# diun.metadata.output_image=zabbix-proxy-mysql
# diun.metadata.output_tag=trunk-alpine
FROM zabbix/zabbix-proxy-mysql:trunk-alpine

# Switch to root (so we can install packages)
USER root

# Install jq, expect, openssh, sshpass, and tini
RUN apk add --update --no-cache jq expect openssh sshpass tini

# Switch back to the zabbix user
USER 1997
