# How do I use tar command line parameters?
// plain

The `tar` command is used to create, modify, and extract archives from various types of files. It is commonly used to compress files for storage or transport.

The basic syntax of the `tar` command is:

```
tar [options] [archive file] [files or directories]
```

The following are some of the commonly used parameters for the `tar` command:

* `-c`: Creates an archive
* `-x`: Extracts files from an archive
* `-t`: Lists the contents of an archive
* `-v`: Displays progress information
* `-f`: Specifies the name and path of the archive file

For example, to create an archive named `myarchive.tar` from the files `file1.txt` and `file2.txt`, the command would be:

```
tar -cf myarchive.tar file1.txt file2.txt
```

To extract the contents of the archive, the command would be:

```
tar -xf myarchive.tar
```

For more information about the `tar` command, see the following links:

* [GNU Tar Manual](https://www.gnu.org/software/tar/manual/tar.html)
* [Linux man page for tar](https://linux.die.net/man/1/tar)

onelinerhub: [How do I use tar command line parameters?](https://onelinerhub.com/cli-tar/how-do-i-use-tar-command-line-parameters)