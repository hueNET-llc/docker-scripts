# dump1090-sdrplay:latest
[![GitHub](https://img.shields.io/badge/GitHub-blue)](https://github.com/hueNET-llc/docker-scripts/tree/master/dump1090-sdrplay) [![Docker Hub Image](https://img.shields.io/docker/v/rafaelwastaken/dump1090-sdrplay/latest)](https://hub.docker.com/repository/docker/rafaelwastaken/dump1090-sdrplay)

[SDRplay dump1090 fork](https://github.com/SDRplay/dump1090) built with SDRplay and RTL-SDR support

Based on `debian:bookworm-slim` with `SDRplay API v3.15.2`

Any additional args will be passed directly to dump1090

`⚠️ The SDRplay API breaks and segfaults a lot on startup. Enable auto-restart on the container so it keeps retrying until it starts properly.`

Example:
```
docker run -d --name dump1090 --restart unless-stopped --privileged --device /dev/bus/usb -v /dev/bus/usb:/dev/bus/usb --tmpfs /run:exec,size=32M rafaelwastaken/dump1090-sdrplay:latest --dev-sdrplay --gain 50 --modeac --max-range 300 --fix --phase-enhance --mlat --forward-mlat --quiet --lat <latitude> --lon <longitude> --net --net-bind-address 0.0.0.0
```