# How do I use the Unix command tar?
// plain

The Unix command `tar` is a utility used to archive multiple files into a single file. It is commonly used for backing up files, transferring files between systems, and compressing files.

Below is an example of how to use the `tar` command to create an archive file from two existing files:

```
tar -cvf archive.tar file1 file2
```

This command will create a new file called `archive.tar` containing the contents of `file1` and `file2`. The flags used in the command are:

* `-c`: Create an archive.
* `-v`: Verbosely list files which are processed.
* `-f`: Use archive file or device ARCHIVE.

To extract files from an existing archive, use the `-x` flag instead of `-c`:

```
tar -xvf archive.tar
```

This command will extract the contents of `archive.tar` into the current working directory.

For more information on the `tar` command, see the [GNU tar manual](https://www.gnu.org/software/tar/manual/html_node/tar_6.html).

onelinerhub: [How do I use the Unix command tar?](https://onelinerhub.com/cli-tar/how-do-i-use-the-unix-command-tar)