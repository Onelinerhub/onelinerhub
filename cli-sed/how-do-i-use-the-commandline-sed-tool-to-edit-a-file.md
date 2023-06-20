# How do I use the commandline sed tool to edit a file?
// plain

The `sed` (stream editor) command line tool can be used to edit a file. This is done by using the `-i` flag when running `sed` and providing an expression to apply to the file.

For example, to replace the word `hello` with `goodbye` in a file named `example.txt`, the following command can be used:

```
sed -i 's/hello/goodbye/g' example.txt
```

This command will replace all occurrences of `hello` with `goodbye` in the `example.txt` file.

The parts of the command are:

- `sed`: The command to run the stream editor.
- `-i`: The flag to indicate that the changes should be applied to the file directly.
- `s/hello/goodbye/g`: The expression that will be applied to the file. This expression is a substitute command, which will replace all occurrences of `hello` with `goodbye`.
- `example.txt`: The name of the file to apply the expression to.

For more information about `sed`, see the following links:

- [Sed Tutorial](https://www.grymoire.com/Unix/Sed.html)
- [GNU Sed Manual](https://www.gnu.org/software/sed/manual/sed.html)

onelinerhub: [How do I use the commandline sed tool to edit a file?](https://onelinerhub.com/cli-sed/how-do-i-use-the-commandline-sed-tool-to-edit-a-file)