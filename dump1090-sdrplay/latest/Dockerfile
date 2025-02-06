# diun.enable=false
FROM debian:bookworm-slim AS build

WORKDIR /opt

COPY ./install_sdrplay.sh /opt/install_sdrplay.sh

RUN apt-get update && \
    apt-get install -y make pkg-config gcc git wget udev sudo librtlsdr-dev libhidapi-libusb0 expect && \
    wget -O sdrplay_installer.run "https://www.sdrplay.com/software/SDRplay_RSP_API-Linux-3.15.2.run" && \
    chmod +x sdrplay_installer.run && \
    chmod +x install_sdrplay.sh && \
    ./install_sdrplay.sh && \
    git clone https://github.com/SDRplay/dump1090 && \
    cd dump1090 && \
    SDRPLAY=1 make dump1090

# diun.enable=true
# diun.metadata.platforms=linux/amd64,linux/arm64
# diun.metadata.output_image=dump1090-sdrplay
# diun.metadata.output_tag=latest
FROM debian:bookworm-slim

# Copy dump1090 from the build stage
COPY --from=build /opt/dump1090 /opt/dump1090
COPY ./run.sh /opt/dump1090/run.sh

# Copy SDRplay API from the build stage
COPY --from=build /opt/sdrplay_api /opt/sdrplay_api
COPY --from=build /usr/local/include /usr/local/include
COPY --from=build /usr/local/lib /usr/local/lib

# Set the working directory to /opt/dump1090
WORKDIR /opt/dump1090

# Install dependencies needed to run dump1090 and make scripts executable
RUN apt-get update && \
    apt-get install -y librtlsdr-dev libhidapi-libusb0 && \
    chmod +x /opt/dump1090/run.sh && \
    chmod +x /opt/sdrplay_api/sdrplay_apiService

WORKDIR /opt/dump1090

ENTRYPOINT [ "/opt/dump1090/run.sh" ]
