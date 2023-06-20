# How do I use the command line to tar a directory?
// plain

The command line utility `tar` is used to create and manipulate tarball archives. To tar a directory, the following command can be used:

```
tar -cvf <archive_name>.tar <directory_name>
```

This command will create a tarball archive named `<archive_name>.tar` from the directory `<directory_name>`.

The following parts are used in the command:

* `tar` - the command line utility used to create and manipulate tarball archives
* `-cvf` - flags used to create a tarball archive
* `<archive_name>.tar` - the name of the tarball archive to create
* `<directory_name>` - the name of the directory to tar

The output of the command will be the list of files that were added to the tarball archive.

## Helpful links

* [GNU tar Manual](https://www.gnu.org/software/tar/manual/html_node/tar_69.html)
* [tar (Unix) - Wikipedia](https://en.wikipedia.org/wiki/Tar_(Unix))

onelinerhub: [How do I use the command line to tar a directory?](https://onelinerhub.com/cli-tar/how-do-i-use-the-command-line-to-tar-a-directory)