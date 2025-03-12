

zid=$1

# TODO: check args are given

# for zid in "$@"; do
    #  check valid zid
#     ...
# done

acc "$1" |
tr ',' '\n' | 
grep -E '[A-Z]{4}[0-9]{4}t[0-3]_Student' |  
sed -E 's/.*([A-Z]{4}[0-9]{4}).*/\1/'
