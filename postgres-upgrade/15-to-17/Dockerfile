# diun.enable=true
# diun.metadata.platforms=linux/amd64,linux/arm64
# diun.metadata.output_image=postgres-upgrade
# diun.metadata.output_tag=15-to-17
FROM postgres:17-trixie

RUN sed -i 's/$/ 15/' /etc/apt/sources.list.d/pgdg.list

RUN set -eux; \
	apt-get update; \
	apt-get install -y --no-install-recommends \
		postgresql-15='15.14-1.pgdg13+1' \
	; \
	rm -rf /var/lib/apt/lists/*

ENV PGBINOLD /usr/lib/postgresql/15/bin
ENV PGBINNEW /usr/lib/postgresql/17/bin

ENV PGDATAOLD /var/lib/postgresql/15/data
ENV PGDATANEW /var/lib/postgresql/17/data

RUN set -eux; \
	mkdir -p "$PGDATAOLD" "$PGDATANEW"; \
	chown -R postgres:postgres /var/lib/postgresql

WORKDIR /var/lib/postgresql

COPY docker-upgrade /usr/local/bin/

ENTRYPOINT ["docker-upgrade"]

# recommended: --link
CMD ["pg_upgrade"]