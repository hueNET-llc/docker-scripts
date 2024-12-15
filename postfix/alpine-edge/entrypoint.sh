#!/bin/sh
# Parse postconf variables
env | grep '^POSTFIX_' | while IFS= read -r var; do
    # Get the config variable name and value
    var_name=$(echo "$var" | sed 's/POSTFIX_\(.*\)=.*/\1/')
    var_value=$(echo "$var" | cut -d'=' -f2-)
    # Set the config variable
    postconf -e "$var_name = $var_value"
done

# Parse postmap variables
for file_name in $(env | grep '^POSTMAP_' | cut -d'=' -f1); do
    # Strip the POSTMAP_ prefix from the file name
    file_name_clean=$(echo "$file_name" | sed 's/^POSTMAP_//')
    # Use printenv to get the full value, preserving newlines
    file_content=$(printenv "$file_name")
    # Write the value to a file named after the file name (without POSTMAP_ prefix)
    echo "$file_content" > "/etc/postfix/$file_name_clean"
    # Postmap the file
    postmap "/etc/postfix/$file_name_clean"
done

# Start postfix in the foreground
exec /usr/sbin/postfix -c /etc/postfix start-fg