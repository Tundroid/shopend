#!/bin/bash

# Directory to scan
directory_to_scan="./"

# Temporary file to store the initial file list
temp_file="/tmp/file_list.txt"

# Get the initial list of files
find "$directory_to_scan" -type f > "$temp_file"

# Infinite loop to check every 30 seconds
while true; do
    # Create a new temporary file for the current iteration
    temp_current="/tmp/file_list_current.txt"
    
    # Get the current list of files
    find "$directory_to_scan" -type f > "$temp_current"

    # Compare the previous list with the current list
    while IFS= read -r file; do
        if [[ ! -f "$file" ]]; then
            git add .
            git commit -m "Cleanup... deleted: $file"
        fi
    done < "$temp_file"

    # Replace the old file list with the current one for the next iteration
    mv "$temp_current" "$temp_file"

    # Wait for 30 seconds before the next iteration
    sleep 5
done
