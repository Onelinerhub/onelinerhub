# How do I compress a file using tar and gzip?
// plain

To compress a file using tar and gzip, follow these steps:

1. Create a tar file of the file or directory you want to compress:
```
tar -cvf <tar-file-name>.tar <file-or-directory-name>
```
This will create a tar file with the name you specified.

2. Compress the tar file using gzip:
```
gzip <tar-file-name>.tar
```
This will create a gzipped tar file with the same name as the tar file, but with the .gz extension.

3. Extract the compressed tar file:
```
tar -xzf <tar-file-name>.tar.gz
```
This will extract the contents of the gzipped tar file.

- `tar`: creates a tar file of the file or directory you want to compress
- `gzip`: compresses the tar file
- `tar -xzf`: extracts the compressed tar file

## Helpful links
- [GNU tar Manual](https://www.gnu.org/software/tar/manual/tar.html)
- [Gzip Manual](https://www.gnu.org/software/gzip/manual/gzip.html)

onelinerhub: [How do I compress a file using tar and gzip?](https://onelinerhub.com/cli-tar/how-do-i-compress-a-file-using-tar-and-gzip)