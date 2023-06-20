# How do I tar and gzip data from stdin?
// plain

Tar is a program used to archive and compress files or directories. Gzip is a program used to compress files. To tar and gzip data from stdin, the following command can be used:

```
$ tar -czf - <input_file>
```

This command will compress the `<input_file>` and output the result to stdout.

The code can be broken down into the following parts:

* `tar` - the program used to archive and compress files
* `-czf` - flags used to indicate that the command should create a tar archive and compress it with gzip
* `-` - the output should be written to stdout
* `<input_file>` - the file to be archived and compressed

The output of this command will be the compressed tar archive written to stdout.

## Helpful links

* [Tar Documentation](https://www.gnu.org/software/tar/manual/html_node/tar_toc.html)
* [Gzip Documentation](https://www.gnu.org/software/gzip/manual/gzip.html)

onelinerhub: [How do I tar and gzip data from stdin?](https://onelinerhub.com/cli-tar/how-do-i-tar-and-gzip-data-from-stdin)