cut -d' ' -f1 students | sort | uniq -c | grep -Ev '^\s+1 '         | sed -E 's/^ +[[:digit:]]+ //'

