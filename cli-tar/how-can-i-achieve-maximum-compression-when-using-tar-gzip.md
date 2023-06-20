# How can I achieve maximum compression when using tar gzip?
// plain

In order to achieve maximum compression when using tar gzip, you can use the following command:
```
tar -zcvf archive_name.tar.gz directory_name
```
This command will create an archive file (archive_name.tar.gz) from the specified directory (directory_name). The 'z' flag indicates that the archive should be compressed with gzip, the 'c' flag indicates that the archive should be created, and the 'v' flag indicates that verbose output should be displayed.

The following list explains the parts of the command:
- tar: The command used to create an archive
- -z: Indicates that the archive should be compressed with gzip
- -c: Indicates that the archive should be created
- -v: Indicates that verbose output should be displayed
- archive_name.tar.gz: The name of the archive file
- directory_name: The name of the directory to be archived

For more information, you can refer to the following links:
- [GNU Tar Manual](https://www.gnu.org/software/tar/manual/tar.html)
- [How to Compress and Extract Files Using Tar Command in Linux](https://www.linuxtechi.com/compress-extract-files-using-tar-command-linux/)

onelinerhub: [How can I achieve maximum compression when using tar gzip?](https://onelinerhub.com/cli-tar/how-can-i-achieve-maximum-compression-when-using-tar-gzip)