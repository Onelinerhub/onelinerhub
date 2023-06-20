# How do I decompress a tar.gz file using gzip?
// plain

Decompressing a tar.gz file using gzip is a simple process. First, the tar.gz file must be downloaded and saved to a location on the computer. Then, the following command can be used to decompress the file:

```
$ tar -xzvf <file_name>.tar.gz
```

This command will extract the file from the tar.gz archive. The parts of this command are:

- `tar`: The tar command is used to create and extract archives from a file or directory.
- `-xzvf`: This option is used to extract the files from the archive.
- `<file_name>`: This is the name of the tar.gz file.

The output of the command should look something like this:

```
$ tar -xzvf <file_name>.tar.gz
x <file_name>/
x <file_name>/<file_1>
x <file_name>/<file_2>
...
```

The files will be extracted from the tar.gz archive and saved in the same directory as the archive.

## Helpful links

- [GNU Tar Manual](https://www.gnu.org/software/tar/manual/html_node/tar_45.html)
- [Gzip Manual](https://www.gnu.org/software/gzip/manual/gzip.html)

onelinerhub: [How do I decompress a tar.gz file using gzip?](https://onelinerhub.com/cli-tar/how-do-i-decompress-a-tar-gz-file-using-gzip)