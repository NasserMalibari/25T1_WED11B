#!/usr/bin/dash

for file in $(find /usr/src/ -type f -name '*.c' ); do
    echo "mutt andrewsEmail  -a $file"
done
