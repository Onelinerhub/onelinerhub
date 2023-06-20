# How do I delete a line using the command line sed tool?
// plain

To delete a line using the command line sed tool, you can use the `d` command. This command will delete the line that matches the pattern that you specify.

For example, if you want to delete the line containing the word "hello" in a file called "example.txt", you can use the following command:

```
sed '/hello/d' example.txt
```

The command will delete the line containing the word "hello" from the file "example.txt".

The parts of the command are as follows:

- `sed`: This is the sed command line tool.
- `/hello/`: This is the pattern that we want to match.
- `d`: This is the command that tells sed to delete the line that matches the pattern.
- `example.txt`: This is the name of the file that we are modifying.

For more information on using the sed command line tool, see the following links:

- [Sed Tutorial](https://www.grymoire.com/Unix/Sed.html)
- [Sed Manual](https://www.gnu.org/software/sed/manual/sed.html)

onelinerhub: [How do I delete a line using the command line sed tool?](https://onelinerhub.com/cli-sed/how-do-i-delete-a-line-using-the-command-line-sed-tool)