# How do I use the CLI tar command?
// plain

The `tar` command (short for Tape Archive) is a powerful command line utility used to create and manipulate archives. It is commonly used to compress large files and directories for storage or for transmission over a network.

To use the `tar` command, the syntax is `tar <options> <archive_name.tar> <files_to_archive>`.

For example, to create an archive of the directory `my_files` and save it to `my_files.tar`, the command would be:

```
tar -cf my_files.tar my_files
```

The options used in this command are:
* `-c`: create an archive
* `-f`: use the filename specified

To extract the contents of the archive, the syntax is `tar -xvf <archive_name.tar>`. The options used in this command are:
* `-x`: extract an archive
* `-v`: verbosely list files processed
* `-f`: use the filename specified

For example, to extract the contents of `my_files.tar`, the command would be:

```
tar -xvf my_files.tar
```

For more information on the `tar` command, see the [GNU tar manual](https://www.gnu.org/software/tar/manual/tar.html).

onelinerhub: [How do I use the CLI tar command?](https://onelinerhub.com/cli-tar/how-do-i-use-the-cli-tar-command)