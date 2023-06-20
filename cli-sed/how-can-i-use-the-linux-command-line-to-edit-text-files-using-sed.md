# How can I use the Linux command line to edit text files using sed?
// plain

The `sed` command is a powerful Linux command line tool used for editing text files. It has many features and can be used to perform a wide range of operations. Here is an example of how to use `sed` to edit a text file:

```
sed -i 's/old/new/g' filename
```

This command replaces all occurrences of the string `old` with the string `new` in the file named `filename`.

Here is a list of the parts of the command:

- `sed`: The command itself.
- `-i`: This option tells `sed` to edit the file in place instead of writing the output to the terminal.
- `s/old/new/g`: This is the substitution command. It tells `sed` to replace all occurrences of `old` with `new`.
- `filename`: The name of the file to be edited.

For more information, see the following links:

- [sed man page](https://linux.die.net/man/1/sed)
- [sed tutorial](https://www.grymoire.com/Unix/Sed.html)

onelinerhub: [How can I use the Linux command line to edit text files using sed?](https://onelinerhub.com/cli-sed/how-can-i-use-the-linux-command-line-to-edit-text-files-using-sed)