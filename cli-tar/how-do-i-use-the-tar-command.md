# How do I use the tar command?
// plain

The `tar` command is a powerful archiving tool used to create, manage, and extract files from a compressed archive. It is commonly used to compress and distribute large files and directories.

To use the `tar` command, you must specify the options you want to use and the name of the archive file. For example, to create an archive file named `my_archive.tar` containing the files `file1.txt` and `file2.txt`, you would use the following command:

```
tar -cf my_archive.tar file1.txt file2.txt
```

To extract the files from the archive, you would use the following command:

```
tar -xf my_archive.tar
```

The options used in the command are as follows:

* `-c`: Create an archive.
* `-f`: Specify the archive filename.
* `-x`: Extract files from the archive.

For more information about the `tar` command, see the [GNU tar manual](https://www.gnu.org/software/tar/manual/html_node/tar_toc.html).

onelinerhub: [How do I use the tar command?](https://onelinerhub.com/cli-tar/how-do-i-use-the-tar-command)