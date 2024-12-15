# diun.enable=false
FROM nginx:mainline-alpine AS build-module

WORKDIR /root

ENV HEADERS_MORE_VERSION="0.34"

ENV FANCY_INDEX_VERSION="0.5.2"

RUN NGINX_VERSION=$(nginx -version 2>&1 | sed -E "s/nginx version: nginx\///") && \
    apk add --no-cache g++ pcre-dev zlib-dev make && \
    wget https://nginx.org/download/nginx-$NGINX_VERSION.tar.gz && \
    tar -xzvf nginx-$NGINX_VERSION.tar.gz && \
    cd nginx-$NGINX_VERSION && \
    wget https://github.com/openresty/headers-more-nginx-module/archive/refs/tags/v$HEADERS_MORE_VERSION.tar.gz && \
    tar -xzvf v$HEADERS_MORE_VERSION.tar.gz && \
    wget https://github.com/aperezdc/ngx-fancyindex/releases/download/v0.5.2/ngx-fancyindex-$FANCY_INDEX_VERSION.tar.xz && \
    tar -xJvf ngx-fancyindex-$FANCY_INDEX_VERSION.tar.xz && \
    ./configure --with-compat --add-dynamic-module=headers-more-nginx-module-$HEADERS_MORE_VERSION --add-dynamic-module=ngx-fancyindex-$FANCY_INDEX_VERSION && \
    make modules -j48 && \
    mkdir /root/modules && \
    mv objs/ngx_http_headers_more_filter_module.so /root/modules && \
    mv objs/ngx_http_fancyindex_module.so /root/modules

# diun.enable=true
# diun.metadata.platforms=linux/amd64,linux/arm64
FROM nginx:mainline-alpine

WORKDIR /root

COPY --from=build-module /root/modules/ /usr/lib/nginx/modules
