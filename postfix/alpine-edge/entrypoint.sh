#!/bin/sh
# Parse config variables
env | grep '^POSTFIX_' | while IFS= read -r var; do
    var_name=$(echo "$var" | sed 's/POSTFIX_\(.*\)=.*/\1/')
    var_value=$(echo "$var" | cut -d'=' -f2-)
    postconf -e "$var_name = $var_value"
done

# Parse map variables
for var_name in $(env | grep '^POSTMAP_' | cut -d'=' -f1); do
    # Strip the POSTMAP_ prefix from the variable name
    var_name_clean=$(echo "$var_name" | sed 's/^POSTMAP_//')
    # Use printenv to get the full value, preserving newlines
    var_value=$(printenv "$var_name")
    # Write the value to a file named after the variable name (without POSTMAP_ prefix)
    echo "$var_value" > "/etc/postfix/$var_name_clean"
    # Postmap the file
    postmap "/etc/postfix/$var_name_clean"
done

# Start postfix in the foreground
exec /usr/sbin/postfix -c /etc/postfix start-fg