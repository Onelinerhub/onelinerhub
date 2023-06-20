# How do I view the header of a tar.gz file?
// plain

You can view the header of a tar.gz file using the command line tool `tar`. This command allows you to view the contents of a tar file without extracting it.

The `-t` flag is used to list the contents of the tar file, and the `-v` flag is used to view the header information.

For example:

```
$ tar -tvf myfile.tar.gz
-rw-r--r--  0 user  staff  1234 Jan 01 00:00 myfile.txt
```

The output of the command will show the header information of the file, including the file permissions, user and group ownership, size, and date modified.

The full syntax for the `tar` command is as follows:

```
tar [OPTION...] [FILE]
```

Where `[OPTION...]` can include any of the following flags:

- `-t`: List the contents of an archive
- `-v`: Verbosely list files processed
- `-f`: Use archive file or device ARCHIVE

For more information on the `tar` command, please refer to the [GNU tar manual](https://www.gnu.org/software/tar/manual/html_node/tar_7.html).

onelinerhub: [How do I view the header of a tar.gz file?](https://onelinerhub.com/cli-tar/how-do-i-view-the-header-of-a-tar-gz-file)