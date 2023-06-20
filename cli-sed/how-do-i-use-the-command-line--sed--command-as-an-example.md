# How do I use the command line 'sed' command as an example?
// plain

The `sed` command is a powerful command line utility that can be used to perform text manipulation and search operations.

For example, to replace the word "foo" with the word "bar" in a file called `example.txt`, you can use the following command:

```
sed -i 's/foo/bar/g' example.txt
```

This command will replace all occurrences of the word "foo" with "bar" in the file `example.txt`.

The parts of the command are as follows:

* `sed` - The command to run the sed utility
* `-i` - The flag to indicate that the changes should be made in-place
* `s/foo/bar/g` - The substitution command, which replaces all occurrences of "foo" with "bar"
* `example.txt` - The file to perform the substitution on

For more information about the `sed` command, you can refer to the [GNU sed Manual](https://www.gnu.org/software/sed/manual/sed.html).

onelinerhub: [How do I use the command line 'sed' command as an example?](https://onelinerhub.com/cli-sed/how-do-i-use-the-command-line--sed--command-as-an-example)