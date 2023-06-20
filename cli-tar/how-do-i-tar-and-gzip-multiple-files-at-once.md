# How do I tar and gzip multiple files at once?
// plain

The `tar` and `gzip` commands can be used together to compress multiple files at once.

To do this, use the following syntax:

```
tar czvf <archive-name.tar.gz> <file1> <file2> <file3> ...
```

Where `<archive-name.tar.gz>` is the name of the resulting archive, and `<file1> <file2> <file3> ...` is a list of files to be compressed.

For example, the following command will compress the `file1.txt`, `file2.txt`, and `file3.txt` files into a single `archive.tar.gz` file:

```
tar czvf archive.tar.gz file1.txt file2.txt file3.txt
```

The `c` flag tells `tar` to create an archive, the `z` flag tells it to compress the archive with `gzip`, the `v` flag tells it to be verbose (i.e. display progress information), and the `f` flag tells it to use the following argument as the archive name.

For more information, see the following links:

- [tar man page](https://linux.die.net/man/1/tar)
- [gzip man page](https://linux.die.net/man/1/gzip)

onelinerhub: [How do I tar and gzip multiple files at once?](https://onelinerhub.com/cli-tar/how-do-i-tar-and-gzip-multiple-files-at-once)