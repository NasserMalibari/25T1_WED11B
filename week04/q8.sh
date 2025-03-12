
./q6.sh |
while read zid; do
    ./q7.sh "$zid"
    # echo "zid is $zid"
done | sort | uniq -c