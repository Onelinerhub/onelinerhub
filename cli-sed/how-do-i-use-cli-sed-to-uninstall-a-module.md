# How do I use CLI sed to uninstall a module?
// plain

Using the `sed` command line interface (CLI) to uninstall a module involves using the `-i` option to make in-place edits to a file. The `-i` option takes a regular expression as an argument. This expression is used to find and replace specific parts of the file.

For example, to uninstall a module called `mymodule`, the following command can be used:

```
sed -i "/mymodule/d" /path/to/module/config.json
```

This command will delete any line containing the string `mymodule` from the file `/path/to/module/config.json`.

The parts of the command are:
* `sed` - the command to run
* `-i` - the option to make in-place edits
* `/mymodule/d` - the regular expression to find and replace
* `/path/to/module/config.json` - the file to edit

## Helpful links
* [Sed Command Tutorial](https://www.guru99.com/sed-command-linux.html)
* [Sed Manual](http://www.grymoire.com/Unix/Sed.html)

onelinerhub: [How do I use CLI sed to uninstall a module?](https://onelinerhub.com/cli-sed/how-do-i-use-cli-sed-to-uninstall-a-module)