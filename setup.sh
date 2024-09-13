#!/bin/bash

PATH_ENV_TEMPLATE="templates/.env.template"
PATH_ENV_DESTINATION=".env"

# Function to check for the presence of the source file
check_file_exists() {
    if [ ! -f "$1" ]; then
        >&2 echo "Error: Source file '$1' does not exist."
        exit 1
    fi
}

# Function to prompt the user about overwriting the destination file
prompt_overwrite() {
    read -p "File '$PATH_ENV_DESTINATION' already exists. Do you want to override it? (y/n): " choice
    case "$choice" in
        y|Y ) echo "Overwriting file...";;
        n|N ) echo "Aborting."; exit 0;;
        * ) echo "Invalid choice. Aborting."; exit 1;;
    esac
}

# Enforce explicit tracking rule to avoid tracking .env
stop_env_tracking() {
    echo "Updating git index to skip worktree for '$PATH_ENV_DESTINATION'"
    if git update-index --skip-worktree "$1"; then
        echo "Successfully updated git index rules"
    else 
        >&2 echo "Error: Failed to update git index to skip worktree for '$PATH_ENV_DESTINATION'."
    fi
}

# Check if the script is running on Unix-like or Windows platform
if [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
    # Windows-like platforms, just force the joiner. Don't check for cygpath
    PATH_ENV_TEMPLATE="templates\\.env.template"
fi

# Check if the source file exists
check_file_exists "$PATH_ENV_TEMPLATE"

# Check if the destination file exists
if [ -f "$PATH_ENV_DESTINATION" ]; then
    echo "'$PATH_ENV_DESTINATION' already exists"
    # stop_env_tracking "$PATH_ENV_DESTINATION"
    prompt_overwrite
else
    # Copy the source file to the destination
    cp "$PATH_ENV_TEMPLATE" "$PATH_ENV_DESTINATION"

    # Check if the copy was successful
    if [ $? -eq 0 ]; then
        echo "File copied successfully."
    else
        >&2 echo "Error: File could not be copied."
        exit 1
    fi
    # stop_env_tracking "$PATH_ENV_DESTINATION"
fi
