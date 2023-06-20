# How do I use gzip, tar, and zip to compress files?
// plain

Gzip, tar, and zip are three popular tools for compressing files.

Gzip is a file compression tool that compresses files to the .gz format. To compress a file with gzip, run the command `gzip <filename>` in the terminal.

Tar is a file archiving and compression tool. To compress a file with tar, run the command `tar -czf <archive-name>.tar.gz <filename>` in the terminal.

Zip is a file archiving and compression tool. To compress a file with zip, run the command `zip <archive-name>.zip <filename>` in the terminal.

For example, to compress a file called `test.txt` with gzip, run the following command:
```
gzip test.txt
```
This will create a compressed file called `test.txt.gz`.

To compress a file called `test.txt` with tar, run the following command:
```
tar -czf test.tar.gz test.txt
```
This will create a compressed file called `test.tar.gz`.

To compress a file called `test.txt` with zip, run the following command:
```
zip test.zip test.txt
```
This will create a compressed file called `test.zip`.

## Helpful links
- [Gzip](https://www.gnu.org/software/gzip/)
- [Tar](https://www.gnu.org/software/tar/)
- [Zip](https://en.wikipedia.org/wiki/Zip_(file_format))

onelinerhub: [How do I use gzip, tar, and zip to compress files?](https://onelinerhub.com/cli-tar/how-do-i-use-gzip--tar--and-zip-to-compress-files)