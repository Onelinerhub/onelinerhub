# How do I use tar in the Windows terminal?
// plain

The tar command in Windows can be used to create and extract tar archives. It is part of the Windows Subsystem for Linux (WSL) and can be accessed through the Windows Terminal.

To create a tar archive, use the following command:
```
tar -czvf archive_name.tar.gz /path/to/directory
```
This command will create a compressed tar archive called `archive_name.tar.gz` from the contents of `/path/to/directory`.

To extract a tar archive, use the following command:
```
tar -xzvf archive_name.tar.gz
```
This command will extract the contents of `archive_name.tar.gz` to the current working directory.

The following options can be used with the tar command:
- `-c`: Create an archive
- `-x`: Extract an archive
- `-z`: Compress the archive using gzip
- `-v`: Verbose output
- `-f`: Specify the filename of the archive

For more information, see the [tar man page](https://linux.die.net/man/1/tar).

onelinerhub: [How do I use tar in the Windows terminal?](https://onelinerhub.com/cli-tar/how-do-i-use-tar-in-the-windows-terminal)