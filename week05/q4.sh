

print_message() {

    # TODO: check num args, with usage message on error
    # check $1 is a number when $# -eq 2

    if [ "$#" -eq 1 ]; then
        echo "WARNING: $1"
    elif [ "$#" -eq 2 ]; then
        echo "ERROR: $2" >&2
        exit "$1"
    fi

    # ex: rewrite with case statements

    # case $# in

    # 1) .... ;;
    # 2) .... ;;
    # *) .... ;;


}

print_message "this is a warning"
print_message 42 "this is an error"
