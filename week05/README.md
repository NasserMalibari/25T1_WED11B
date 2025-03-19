
# 1
Write a shell script `extract.sh` that, when given one or more archive files as command line arguments, will use the correct program to extract the files. 

### Notes
- Note the recommended way how to loop through command line arguments
- How can case statements help us distinguish the file types of the command line arguments?

# 2
 Given an anonymous list of CSE logins.

Write a shell script last.sh that, using shell case statments, finds the number of loggins that occurred from within UNSW.
(Look for connections to from the uniwide network)

Additionally, find the distribution of zIDs by their first digit. 

### Notes
- Review the syntax for the patterns we can use for `case` statements.

# 3
Write a shell function top_and_bottom that, given a file name, prints the file name, plus the first and last lines of the file. 

### Notes
- Review how to define a shell function, how do we pass arguments to the function, 
and how do we reference given arguments in the function?
- The function is a filtering task, how can we get the first and last line?
- head/tail may be problematic, could we use `sed` instead?


# 4
 Write a shell function print_message that, given an optional exit status and a message:

If no exit status is given the program should print a warning
If an exit status is given the program should print an error and exit the program 

### Notes
- Task requires us to write a shell function
- We only need to check the number of arguments to the function, and (optionally) use
`exit`.
- How do we write to stderr instead of (or as well as) stdout.

# 5
 Create a git repository called cs2041-Labs and add you week01 and week02 lab work.

Then push your repository to the [CSE gitlab servers](https://nw-syd-gitlab.cseunsw.tech/users/sign_in).

When logging in to the CSE gitlab, make sure you use the "UNSW" tab.
Not the "Standard" tab. 

# 6
 There is a git repository located on the CSE gitlab servers at https://nw-syd-gitlab.cseunsw.tech/cs2041/24t2-tut05
Clone this repository to your local machine. 


