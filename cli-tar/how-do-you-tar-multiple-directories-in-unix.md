# How do you tar multiple directories in Unix?
// plain

Tar is a command line utility used to create and manipulate tar archives in Unix systems.

To tar multiple directories in Unix, use the following command:

```
tar -cvf archive_name.tar dir1 dir2 dir3
```

This command will create a tar archive named `archive_name.tar` containing the content of the directories `dir1`, `dir2` and `dir3`.

The flags used in this command are:
- `-c`: create a new tar archive
- `-v`: verbose output, display the progress of the archiving process
- `-f`: specify the name of the tar archive

For more information, refer to the [GNU tar manual](https://www.gnu.org/software/tar/manual/tar.html).

onelinerhub: [How do you tar multiple directories in Unix?](https://onelinerhub.com/cli-tar/how-do-you-tar-multiple-directories-in-unix)