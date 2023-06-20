# How do I compress a single file using tar and gzip?
// plain

Compressing a single file using tar and gzip requires two steps:

1. Create a tar file containing the file to be compressed:
```
tar -cf <file_name>.tar <file_to_compress>
```
This command will create a tar file named `<file_name>.tar` containing the file `<file_to_compress>`.

2. Compress the tar file using gzip:
```
gzip <file_name>.tar
```
This command will compress the tar file, creating a file named `<file_name>.tar.gz`.

The resulting `<file_name>.tar.gz` file is the compressed version of the original file.

## Code explanation

- `tar -cf <file_name>.tar <file_to_compress>`: creates a tar file containing the file to be compressed
- `gzip <file_name>.tar`: compresses the tar file using gzip

## Helpful links
- [GNU Tar manual](https://www.gnu.org/software/tar/manual/tar.html)
- [Gzip manual](https://www.gnu.org/software/gzip/manual/gzip.html)

onelinerhub: [How do I compress a single file using tar and gzip?](https://onelinerhub.com/cli-tar/how-do-i-compress-a-single-file-using-tar-and-gzip)