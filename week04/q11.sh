

program_name="$1"
flag=0

for path in $(echo "$PATH" | tr ':' ' '); do  # path1:path    -> 'path 1' path2
    # echo "$path"
    # echo "$path$program_name"
    if [ -x "$path/$program_name" ]; then
        flag=1
        ls -l "$path/$program_name"
    fi
done


if [ $flag -eq 0 ]; then
    echo "$program_name not found"
fi
