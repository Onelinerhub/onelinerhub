# How can I use tar commands in Linux?
// plain

The `tar` command in Linux is used to create, view, modify, and extract files from an archive file. It is one of the most commonly used commands for archiving and compressing files.

To create an archive file using the `tar` command, use the following syntax:

```
tar -cvf archive_name.tar file1 file2 file3
```

This will create an archive file named `archive_name.tar` that contains the files `file1`, `file2`, and `file3`.

To view the contents of an existing archive file, use the following syntax:

```
tar -tvf archive_name.tar
```

This will list the files and directories in the archive.

To extract the contents of an existing archive file, use the following syntax:

```
tar -xvf archive_name.tar
```

This will extract the contents of the archive to the current directory.

To modify an existing archive file, use the following syntax:

```
tar -uvf archive_name.tar file4
```

This will add the file `file4` to the existing archive file `archive_name.tar`.

For more information on the `tar` command, see the [GNU Tar Manual](https://www.gnu.org/software/tar/manual/html_node/tar_toc.html).

onelinerhub: [How can I use tar commands in Linux?](https://onelinerhub.com/cli-tar/how-can-i-use-tar-commands-in-linux)