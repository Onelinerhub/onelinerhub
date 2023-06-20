# How do tar gzip and zip differ in terms of file compression?
// plain

Tar, Gzip and Zip are three different methods of compressing files.

**Tar** is a file archiving utility that combines multiple files into a single file. It is not a compression utility, but it can be used in conjunction with a compression utility such as Gzip to compress the archived file.

**Gzip** is a compression utility that compresses a single file. It is usually used to compress text files, but can be used to compress any type of file.

**Zip** is a file archiving utility that combines multiple files into a single file and compresses them. It is more efficient than Tar and Gzip combined.

The following example shows how to use Tar, Gzip and Zip to compress a directory of files:

```
# Compress a directory of files using Tar, Gzip and Zip
tar -cvf directory.tar directory/
gzip directory.tar
zip -r directory.zip directory/
```

The example code will produce two files: `directory.tar.gz` and `directory.zip`. `directory.tar.gz` is a compressed Tar archive and `directory.zip` is a compressed Zip archive.

## Code explanation

  * `tar -cvf directory.tar directory/`: This command creates a Tar archive of the `directory` folder and saves it as `directory.tar`.
  * `gzip directory.tar`: This command compresses the `directory.tar` file using Gzip.
  * `zip -r directory.zip directory/`: This command creates a Zip archive of the `directory` folder and saves it as `directory.zip`.

* ## Helpful links
  * [Tar Command](https://linux.die.net/man/1/tar)
  * [Gzip Command](https://linux.die.net/man/1/gzip)
  * [Zip Command](https://linux.die.net/man/1/zip)

onelinerhub: [How do tar gzip and zip differ in terms of file compression?](https://onelinerhub.com/cli-tar/how-do-tar-gzip-and-zip-differ-in-terms-of-file-compression)