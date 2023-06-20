# How do I compress a tar file using gzip?
// plain

Compressing a tar file using gzip is a two-step process. First, you must create a tar file and then compress it using gzip.

To create a tar file, use the following command:

```
tar -cvf name_of_archive.tar /path/to/files
```

This command will create an archive named `name_of_archive.tar` in the current directory containing all of the files and directories located in `/path/to/files`.

To compress the tar file using gzip, use the following command:

```
gzip name_of_archive.tar
```

This will create a compressed version of the tar file, named `name_of_archive.tar.gz`.

Parts of the command:

* `tar` - The tar command is used to create, maintain, and modify archives.
* `-cvf` - These flags are used to create a tar archive.
* `name_of_archive.tar` - This is the name of the tar archive that will be created.
* `/path/to/files` - This is the path to the directory containing the files that will be archived.
* `gzip` - The gzip command is used to compress and decompress files.
* `name_of_archive.tar.gz` - This is the name of the compressed tar file that will be created.

## Helpful links

* [GNU tar Manual](https://www.gnu.org/software/tar/manual/tar.html)
* [GNU gzip Manual](https://www.gnu.org/software/gzip/manual/gzip.html)

onelinerhub: [How do I compress a tar file using gzip?](https://onelinerhub.com/cli-tar/how-do-i-compress-a-tar-file-using-gzip)