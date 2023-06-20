# How can I tar and gzip a file in one command?
// plain

The `tar` command can be used to tar and gzip a file in one command. To do this, use the `-z` option flag to compress the file using gzip. The syntax for this command is:

```
tar -zcvf <filename>.tar.gz <file>
```

This will create a `<filename>.tar.gz` file in the current directory.

## Code explanation


* `tar`: the command used to tar and gzip a file
* `-z`: the option flag to compress the file using gzip
* `cvf`: the options flags to create a tar file, verbose output, and specify the output file name
* `<filename>.tar.gz`: the output file name
* `<file>`: the name of the file to be compressed

For more information about the tar command, see the following links:

* [GNU tar Manual](https://www.gnu.org/software/tar/manual/tar.html)
* [Linux tar command](https://linuxize.com/post/linux-tar-command/)

onelinerhub: [How can I tar and gzip a file in one command?](https://onelinerhub.com/cli-tar/how-can-i-tar-and-gzip-a-file-in-one-command)