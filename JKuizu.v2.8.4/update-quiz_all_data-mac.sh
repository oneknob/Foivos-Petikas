#!/bin/bash

# Set the URL of the file to be downloaded
file_url="https://docs.google.com/spreadsheets/d/1gd39s6qk4QlvLr-mlJgii67-tbycbQ4m/export?format=csv"

# Set the name of the file to be saved
downloaded_file="quiz_all_data.csv"

# Download the file
curl -o "$downloaded_file" "$file_url"

# Replace the existing file with the downloaded one, if it exists
if [ -e "$downloaded_file" ]; then
    cp -f "$downloaded_file" "$(dirname "$0")/$downloaded_file"
    echo "File download and replacement complete."
else
    echo "Failed to download the file."
fi

