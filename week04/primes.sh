


# TODO: check num is an int and > 2
num="$1"
i=2

while [ "$i" -lt "$num" ]; do
    if ./is_prime.sh $i > /dev/null; then 
        echo "$i"
    fi
    i=$((i + 1))

done