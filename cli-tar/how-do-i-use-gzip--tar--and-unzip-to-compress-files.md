# How do I use gzip, tar, and unzip to compress files?
// plain

Using gzip, tar, and unzip to compress files is relatively simple.

Using gzip, you can compress a single file with the following command:
```
gzip <filename>
```
This will create a new file with a .gz extension.

Using tar, you can compress multiple files into a single file with the following command:
```
tar -cvf <archive_name>.tar <files_to_archive>
```
This command will create an archive file with a .tar extension.

Using unzip, you can extract the contents of a compressed file with the following command:
```
unzip <filename>.zip
```
This command will extract the contents of the compressed file into the current directory.

## Code explanation

- gzip: Compress a single file
- tar: Compress multiple files into a single file
- unzip: Extract the contents of a compressed file

## Helpful links
- [gzip Manual](https://www.gnu.org/software/gzip/manual/gzip.html)
- [tar Manual](https://www.gnu.org/software/tar/manual/tar.html)
- [unzip Manual](https://linux.die.net/man/1/unzip)

onelinerhub: [How do I use gzip, tar, and unzip to compress files?](https://onelinerhub.com/cli-tar/how-do-i-use-gzip--tar--and-unzip-to-compress-files)