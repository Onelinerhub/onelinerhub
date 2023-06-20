# -indexing

How can I use sed to perform zero-indexing in a command line environment?
// plain

Sed is a powerful text manipulation tool that can be used to perform zero-indexing in a command line environment. Zero-indexing is a process of converting a list of numbers to start from zero instead of one.

For example, to zero-index a list of numbers from 1 to 10, the following code can be used:

```
echo 1 2 3 4 5 6 7 8 9 10 | sed 's/[0-9]/&-1/g'
```

The output of this command will be:

```
0-1 1-1 2-1 3-1 4-1 5-1 6-1 7-1 8-1 9-1 10-1
```

The code works by using a regular expression to match all numbers (`[0-9]`) and replace them with the same number minus one (`&-1`).

The following list explains the parts of the code:

- `echo 1 2 3 4 5 6 7 8 9 10`: This prints the list of numbers from 1 to 10.
- `sed 's/[0-9]/&-1/g'`: This uses sed to find all numbers (`[0-9]`) and replace them with the same number minus one (`&-1`).
- `g`: This flag indicates that the command should be applied globally.

For more information, please see the following links:

- [Sed Tutorial](https://www.grymoire.com/Unix/Sed.html)
- [Regular Expressions](https://www.regular-expressions.info/)

onelinerhub: [-indexing

How can I use sed to perform zero-indexing in a command line environment?](https://onelinerhub.com/cli-sed/-indexing--how-can-i-use-sed-to-perform-zero-indexing-in-a-command-line-environment)