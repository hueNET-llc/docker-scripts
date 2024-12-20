# postfix:alpine-3.21
[![Docker Hub Image](https://img.shields.io/docker/v/rafaelwastaken/postfix/alpine-3.21)](https://hub.docker.com/repository/docker/rafaelwastaken/postfix)

Alpine-based postfix with lmdb & sasl support

Environment Variables:
- Beginning with `POSTFIX_` will automatically be inserted into `main.cf`
  - Example: `POSTFIX_mydomain=test.com` will be inserted as `mydomain = test.com` in main.cf
- Beginning with `POSTMAP_` will automatically be postmap'd into `/etc/postfix`

Examples:
- `POSTFIX_[config name]=[config value]` - Imported with `postconf -e "[config name] = [config value]"`
- `POSTMAP_[filename] = [file content]` - File is automatically generated and imported with `postmap /etc/postfix/[filename]`