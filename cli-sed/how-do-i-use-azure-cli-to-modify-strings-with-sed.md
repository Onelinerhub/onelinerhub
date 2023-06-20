# How do I use Azure CLI to modify strings with sed?
// plain

The Azure CLI provides a powerful command line interface for managing Azure resources. It can also be used to modify strings with the `sed` command. `sed` is a stream editor that can be used to perform basic text transformations on an input stream.

For example, to replace all occurrences of the word "foo" with the word "bar" in a file named "input.txt", the following command can be used:
```
$ sed -i 's/foo/bar/g' input.txt
```

The command has the following parts:
- `sed`: the command to invoke the stream editor
- `-i`: the option to edit the file in place
- `s/foo/bar/g`: the substitution command, which replaces all occurrences of "foo" with "bar"
- `input.txt`: the file to be modified

For more information, see the [sed manual page](https://www.gnu.org/software/sed/manual/sed.html) and the [Azure CLI documentation](https://docs.microsoft.com/en-us/cli/azure/).

onelinerhub: [How do I use Azure CLI to modify strings with sed?](https://onelinerhub.com/cli-sed/how-do-i-use-azure-cli-to-modify-strings-with-sed)