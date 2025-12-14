lsusb | grep -i "sdrplay" | while read -r line; do
    case "$line" in
        *"$TARGET_ID"*)
            # Extract Bus and Device safely
            bus=$(echo "$line" | awk '{print $2}')
            dev=$(echo "$line" | awk '{print $4}' | tr -d ':')
            
            devpath="/dev/bus/usb/$bus/$dev"
            
            if [ -c "$devpath" ]; then
                /opt/usb_reset "$devpath"
                echo "Reset SDRplay device: $line"
            else
                echo "Error: Device $devpath not accessible."
            fi
            ;;
        *)
            # Do nothing for non-matching devices
            ;;
    esac
done
