# How can I use the command line to print the output of a sed command?
// plain

You can use the command line to print the output of a sed command by using the `-n` flag. This flag suppresses the default output of sed, and instead prints only the output specified in the command.

For example, the following command prints the lines containing the word "example" from a file called `example.txt`:
```
sed -n '/example/p' example.txt
```
The output of this command might look like this:
```
This is an example line
This is another example line
```

The parts of the command are as follows:
* `sed`: the command used to stream-edit files
* `-n`: the flag to suppress default output
* `/example/p`: the pattern to match and the `p` command to print the line
* `example.txt`: the file to be edited

For more information, see the [GNU sed manual](https://www.gnu.org/software/sed/manual/sed.html).

onelinerhub: [How can I use the command line to print the output of a sed command?](https://onelinerhub.com/cli-sed/how-can-i-use-the-command-line-to-print-the-output-of-a-sed-command)