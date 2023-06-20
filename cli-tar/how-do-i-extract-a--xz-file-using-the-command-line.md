# How do I extract a .xz file using the command line?
// plain

The `xz` command line utility can be used to extract `.xz` files.

To extract a `.xz` file, the command is `xz -d <filename>.xz`.

For example, to extract a file named `example.xz`, the command would be:

```
xz -d example.xz
```

This will extract the file and create a new file with the same name but without the `.xz` extension.

The command consists of the following parts:

* `xz`: The command to run the `xz` utility.
* `-d`: The flag to tell `xz` to decompress the file.
* `example.xz`: The name of the `.xz` file to be extracted.

For more information, see the following links:

* [xz man page](https://linux.die.net/man/1/xz)
* [xz Wikipedia page](https://en.wikipedia.org/wiki/Xz)

onelinerhub: [How do I extract a .xz file using the command line?](https://onelinerhub.com/cli-tar/how-do-i-extract-a--xz-file-using-the-command-line)