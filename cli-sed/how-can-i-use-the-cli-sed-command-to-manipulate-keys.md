# How can I use the CLI sed command to manipulate keys?
// plain

The `sed` command is a powerful command line utility that can be used to manipulate keys. It can be used to search and replace text, delete lines, and more. Here is an example of how to use `sed` to search for a key and replace it with a new one:

```
sed -i 's/old_key/new_key/g' filename
```

This command will search for all occurrences of `old_key` in `filename` and replace them with `new_key`.

Here are some of the parts of the command:

* `sed` – the command itself
* `-i` – the flag to indicate that the file should be edited in-place
* `s/old_key/new_key/g` – the search and replace command, where `old_key` is the text to be replaced and `new_key` is the replacement
* `filename` – the file to be edited

For more information on how to use `sed`, see the following resources:

* [GNU Sed Manual](https://www.gnu.org/software/sed/manual/sed.html)
* [Sed Tutorial](https://www.grymoire.com/Unix/Sed.html)
* [Sed Command Examples](https://www.cyberciti.biz/faq/sed-command-examples/)

onelinerhub: [How can I use the CLI sed command to manipulate keys?](https://onelinerhub.com/cli-sed/how-can-i-use-the-cli-sed-command-to-manipulate-keys)