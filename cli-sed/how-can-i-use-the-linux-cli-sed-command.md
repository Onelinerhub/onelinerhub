# How can I use the Linux CLI sed command?
// plain

The `sed` command is a powerful tool for editing text files from the Linux command line. It can be used to search, replace, and manipulate text.

Here is an example of using `sed` to replace "Hello" with "Goodbye" in a file named "myfile.txt":

```
sed -i 's/Hello/Goodbye/g' myfile.txt
```

The command has the following parts:

- `sed`: The command to invoke the sed utility
- `-i`: The flag to modify the file in-place
- `s/Hello/Goodbye/g`: The search and replace expression, which looks for "Hello" and replaces it with "Goodbye"
- `myfile.txt`: The name of the file to process

This command will modify the file in place, meaning that the original file will be replaced with the modified version.

For more information about the `sed` command, see the following links:

- [Sed manual](https://www.gnu.org/software/sed/manual/sed.html)
- [Sed tutorial](https://www.grymoire.com/Unix/Sed.html)

onelinerhub: [How can I use the Linux CLI sed command?](https://onelinerhub.com/cli-sed/how-can-i-use-the-linux-cli-sed-command)