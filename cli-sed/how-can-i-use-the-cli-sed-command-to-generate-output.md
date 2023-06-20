# How can I use the CLI sed command to generate output?
// plain

The `sed` command is a powerful command line tool for manipulating text files. It can be used to generate output from a given input.

For example, to print the first line of a file, the following command can be used:
```
sed -n '1p' file.txt
```
This will output the first line of the file `file.txt`:
```
This is the first line of the file.
```

The command consists of the following parts:
- `sed`: The command itself.
- `-n`: Suppress default output.
- `1p`: Print the first line of the file.
- `file.txt`: The file from which the output should be generated.

Other common uses of `sed` include replacing text in a file, deleting lines of text, and inserting text into a file. For more information, see the [GNU sed manual](https://www.gnu.org/software/sed/manual/sed.html).

onelinerhub: [How can I use the CLI sed command to generate output?](https://onelinerhub.com/cli-sed/how-can-i-use-the-cli-sed-command-to-generate-output)