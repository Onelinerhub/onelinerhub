# How can I use sed in the command line on a Mac?
// plain

Sed is a powerful command-line text editor that can be used to manipulate text on Mac OS X. It is a stream editor, meaning it can be used to edit files or output from other commands.

To use sed on the command line, you must first open a terminal window. Once you have opened the terminal window, you can use the following command syntax to edit a file:

```
sed 's/old/new/g' filename
```

This command will replace all occurrences of the string "old" with the string "new" in the file specified by "filename".

You can also use sed to edit the output of other commands. For example, this command will print the contents of a file, replacing all occurrences of the string "old" with the string "new":

```
cat filename | sed 's/old/new/g'
```

The command syntax can be modified to perform a variety of text transformations. For example, you can delete lines, add lines, substitute multiple strings, and more.

## Code explanation


- `sed` - the command
- `s/old/new/g` - the substitution command, which replaces all occurrences of the string "old" with the string "new"
- `filename` - the file to be edited
- `cat filename` - the command to print the contents of a file
- `|` - the pipe symbol, which is used to redirect the output of one command to the input of another command

## Helpful links

- [Sed Tutorial](https://www.grymoire.com/Unix/Sed.html)
- [Sed Command Examples](https://www.computerhope.com/unix/used.htm)

onelinerhub: [How can I use sed in the command line on a Mac?](https://onelinerhub.com/cli-sed/how-can-i-use-sed-in-the-command-line-on-a-mac)