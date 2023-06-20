# How do I use a gzip tar pipe to compress files?
// plain

A gzip tar pipe is a way to compress files using the gzip and tar commands together. To use it, you must first create a tar archive of the files you want to compress. You can do this with the following command:

```
tar -cvf archive.tar /path/to/files
```

This will create a `archive.tar` file in the current directory. To compress this file using gzip, you can use the following command:

```
gzip -c archive.tar > archive.tar.gz
```

This will create a new file called `archive.tar.gz` which is a compressed version of the original `archive.tar` file.

## Code explanation


1. `tar -cvf archive.tar /path/to/files`: This command creates a tar archive of the files in the specified directory.
2. `gzip -c archive.tar > archive.tar.gz`: This command compresses the tar archive using gzip and saves it as a new file.

## Helpful links

- [GNU Tar Manual](https://www.gnu.org/software/tar/manual/html_node/tar_91.html)
- [Gzip Manual](https://www.gnu.org/software/gzip/manual/gzip.html)

onelinerhub: [How do I use a gzip tar pipe to compress files?](https://onelinerhub.com/cli-tar/how-do-i-use-a-gzip-tar-pipe-to-compress-files)