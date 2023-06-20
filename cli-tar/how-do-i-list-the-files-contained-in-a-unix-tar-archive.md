# How do I list the files contained in a Unix tar archive?
// plain

To list the files contained in a Unix tar archive, the `tar` command can be used. This command has the `-tvf` flags, which stands for "list verbosely, the contents of an archive file". An example of this command is shown below:

```
tar -tvf archive.tar
```

This command will produce an output similar to this:

```
-rw-r--r-- user/group    0 2020-07-20 11:55 file1.txt
-rw-r--r-- user/group    0 2020-07-20 11:55 file2.txt
-rw-r--r-- user/group    0 2020-07-20 11:55 file3.txt
```

The output of this command will list each file contained in the tar archive, including the file's size, date, and permissions.

The command used is composed of the following parts:

- `tar`: the command to list the contents of a tar archive
- `-tvf`: the flags to list the contents of an archive file verbosely
- `archive.tar`: the name of the tar archive

For more information, please refer to the following links:

- [GNU Tar Manual](https://www.gnu.org/software/tar/manual/html_node/Listing-Contents.html)
- [Linux Commands Cheat Sheet](https://www.cheatography.com/davechild/cheat-sheets/linux-command-line/)

onelinerhub: [How do I list the files contained in a Unix tar archive?](https://onelinerhub.com/cli-tar/how-do-i-list-the-files-contained-in-a-unix-tar-archive)