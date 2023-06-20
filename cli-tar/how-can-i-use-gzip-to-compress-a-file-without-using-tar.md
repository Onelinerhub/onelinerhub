# How can I use gzip to compress a file without using tar?
// plain

Gzip is a file format used for file compression and decompression. It can be used to compress a single file without using tar. To do so, the `gzip` command can be used. For example, to compress a file named `file.txt` the following command can be used:

```
gzip file.txt
```

This will create a new file named `file.txt.gz` containing the compressed version of the original file. The original file will remain unchanged.

The following command can be used to decompress the compressed file:

```
gunzip file.txt.gz
```

This will create a new file named `file.txt` containing the decompressed version of the original file.

The parts of the command are as follows:

- `gzip`: the command to compress a file
- `file.txt`: the name of the file to be compressed
- `gunzip`: the command to decompress a file
- `file.txt.gz`: the name of the compressed file

## Helpful links

- [gzip Manual](https://www.gnu.org/software/gzip/manual/gzip.html)
- [gunzip Manual](https://www.gnu.org/software/gzip/manual/gzip.html#gunzip-invocation)

onelinerhub: [How can I use gzip to compress a file without using tar?](https://onelinerhub.com/cli-tar/how-can-i-use-gzip-to-compress-a-file-without-using-tar)