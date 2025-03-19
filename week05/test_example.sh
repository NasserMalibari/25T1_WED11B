#! /usr/bin/env dash

# ==============================================================================
# test0.sh
# Testing the order of take-submit when multiple inputs are invalid.
#
# Written by: Dylan Brotherston <d.brotherston@unsw.edu.au>
# Date: 2025-03-10
# For COMP2041/9044 Assignment 1
# ==============================================================================

# add the current directory to the PATH so scripts
# can still be executed from it after we cd

PATH="$PATH:$(pwd)"

# Create a temporary directory for the test.
test_dir="$(mktemp -d)"
cd "$test_dir" || exit 1
ref_dir="$(mktemp -d)"
cd "$ref_dir" || exit 1

# Create some files to hold output.

expected_stdout="$(mktemp)"
expected_stderr="$(mktemp)"
actual_stdout="$(mktemp)"
actual_stderr="$(mktemp)"

# Remove the temporary directory when the test is done.

trap 'rm "$expected_stdout" "$expected_stderr" "$actual_stdout" "$actual_stderr" -r "$test_dir"' INT HUP QUIT TERM EXIT

2041 fetch take > /dev/null

cd "$ref_dir" || exit 1
2041 take-add 1 2 3 > "$expected_stdout" 2> "$expected_stderr"

cd "$test_dir" || exit 1
take-add 1 2 3 > "$actual_stdout" 2> "$actual_stderr"

if ! diff $expected_stdout $actual_stdout; then
    echo "Test failed: stdout differs"
    exit 1
fi

if ! diff $expected_stderr $actual_stderr; then
    echo "Test failed: stdout differs"
    exit 1
fi

# an example test case may run these commands and check output is correct
# take-add lab1 multiply.sh multiply.marking multiply.marking
# take-submit 'lab1' '1234567' 'foobar' # test correct error message is received


echo "All tests passed!"

# cat "$expected_stderr"