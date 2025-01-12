#!/bin/bash
# Start the SDRplay service in the background
nohup /opt/sdrplay_api/sdrplay_apiService & \
# Wait 5 seconds for the SDRplay service to start
sleep 5 && \
# Start dump1090 and passthrough all args to it
/opt/dump1090/dump1090 $@ 
