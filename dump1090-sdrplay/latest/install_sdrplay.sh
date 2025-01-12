#!/usr/bin/expect
# Automate the installation of the SDRplay API using expect
spawn /opt/sdrplay_installer.run
expect -timeout 60 "Press RETURN to view the license agreement"
send -- "\r"
expect -timeout 60 "Press space to continue, 'q' to quit."
send -- "q\r"
expect -timeout 60 "the installation, or press n and RETURN to exit the installer"
send -- "y\r"
expect -timeout 60 "or press n and RETURN to change them"
send -- "y\r"
