# How do I use tar to exclude a directory in Unix?
// plain

Using the `tar` command in Unix, you can exclude a directory from being archived. This is done by using the `--exclude` option, followed by the directory name you want to exclude.

For example, to exclude a directory named `foo` from being archived, you would use the following command:

```
tar --exclude=foo -cvf archive.tar .
```

This command would create an archive named `archive.tar` containing all files and directories in the current working directory, except for the `foo` directory.

The parts of the command are:
* `tar` - The tar command
* `--exclude=foo` - The `--exclude` option, followed by the directory name to exclude
* `-cvf` - The flags used to create the archive, `-c` for create, `-v` for verbose, and `-f` to specify the archive filename
* `archive.tar` - The name of the archive
* `.` - The directory to archive

For more information on the `tar` command, see the [man page](http://man7.org/linux/man-pages/man1/tar.1.html).

onelinerhub: [How do I use tar to exclude a directory in Unix?](https://onelinerhub.com/cli-tar/how-do-i-use-tar-to-exclude-a-directory-in-unix)