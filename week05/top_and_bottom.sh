
top_and_bottom() {

    # TODO: arg checking
    
    if [ ! -f "$1" ]; then
        echo "$1 doesnt exist!" >&2
        exit 1
    fi
    
    filename=$1
    echo "filename is $filename"
    head -1 "$filename"
    tail -1 "$filename"
    # sed -n '1p;$p' "$filename" # alternative
    
    
    # local x # not posix **technically

    # echo "arg1 is $1"
    # echo "arg2 is $2"
    # echo "$x"
    # x=3
    # if [ "$#" -ne 2 ]
    
}

# x=2
top_and_bottom "$1"
# x is now 3
