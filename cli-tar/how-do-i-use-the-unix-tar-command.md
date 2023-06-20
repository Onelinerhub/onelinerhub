# How do I use the Unix tar command?
// plain

The Unix tar command is used to create and extract archives. It stands for Tape ARchive and is commonly used to compress multiple files into a single file or to extract files from an archive.

Here is an example of how to use the tar command to create an archive:

```
tar -cvf archive.tar file1 file2 file3
```

This command will create an archive named archive.tar with the files file1, file2, and file3. The flags used in the command are:

* `-c`: Create an archive.
* `-v`: Verbosely list files which are processed.
* `-f`: Use archive file or device ARCHIVE.

To extract files from an archive, the `-x` flag is used instead of `-c` like this:

```
tar -xvf archive.tar
```

This command will extract the files from the archive.tar archive.

For more information about the tar command, see the [GNU tar manual](https://www.gnu.org/software/tar/manual/html_node/tar_toc.html).

onelinerhub: [How do I use the Unix tar command?](https://onelinerhub.com/cli-tar/how-do-i-use-the-unix-tar-command)