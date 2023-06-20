# How do I use gzip and tar in Linux?
// plain

Gzip and tar are two command line tools used to compress and archive files in Linux.

To use gzip, you can run the following command:
```
gzip <filename>
```
This will compress the file and create a new file with a .gz extension.

To unzip the file, you can run the following command:
```
gunzip <filename.gz>
```
This will decompress the file and create a new file with the original filename.

To use tar, you can run the following command to create an archive:
```
tar -cvf <archive_name.tar> <filename1> <filename2> ...
```
This will create a tar archive containing the specified files.

To extract the files from the archive, you can run the following command:
```
tar -xvf <archive_name.tar>
```
This will extract the files from the archive and create new files with the original filenames.

## Code explanation

- `gzip <filename>`: Compress a file and create a new file with a .gz extension
- `gunzip <filename.gz>`: Decompress a file and create a new file with the original filename
- `tar -cvf <archive_name.tar> <filename1> <filename2> ...`: Create a tar archive containing the specified files
- `tar -xvf <archive_name.tar>`: Extract the files from the archive and create new files with the original filenames

## Helpful links
- [Gzip](https://linux.die.net/man/1/gzip)
- [Tar](https://linux.die.net/man/1/tar)

onelinerhub: [How do I use gzip and tar in Linux?](https://onelinerhub.com/cli-tar/how-do-i-use-gzip-and-tar-in-linux)