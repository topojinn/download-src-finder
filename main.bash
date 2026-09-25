#!/bin/bash

FOLDER_PATH="folder placeholder"
FILE_PATH="path placeholder"
LEGIT_DOMAIN_1="domain placeholder 1"
LEGIT_DOMAIN_2="domain placeholder 2"

SOURCE_URL=$(xattr -p com.apple.metadata:kMDItemWhereFroms "$FILE_PATH" 2>/dev/null || \
              getfattr -d -m user.xdg.referrer.url "$FILE_PATH" 2>/dev/null)

if [[ "$SOURCE_URL" == *"$LEGIT_DOMAIN_1"* ]] || [[ "$SOURCE_URL" == *"$LEGIT_DOMAIN_2"* ]]; then
    :
else
    rm -rf "$FOLDER_PATH"
fi
