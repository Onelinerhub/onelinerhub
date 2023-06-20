# How do I use tar commands on Linux?
// plain

The `tar` command is a powerful tool used to create and extract archives on Linux systems.

To create an archive, use the following command:
```
tar -cvf <name_of_archive>.tar <files_to_archive>
```
The `-c` option creates a new archive, `-v` enables verbose output, and `-f` specifies the filename of the archive.

To extract an archive, use the following command:
```
tar -xvf <name_of_archive>.tar
```
The `-x` option extracts the contents of the archive, and `-v` again enables verbose output.

The following options are also useful when working with `tar`:
* `-z`: Compress the archive using gzip
* `-j`: Compress the archive using bzip2
* `-C`: Extract the archive to a specified directory

For more information about `tar` and its options, please refer to the [tar man page](http://man7.org/linux/man-pages/man1/tar.1.html).

onelinerhub: [How do I use tar commands on Linux?](https://onelinerhub.com/cli-tar/how-do-i-use-tar-commands-on-linux)