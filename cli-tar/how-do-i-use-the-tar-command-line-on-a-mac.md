# How do I use the tar command line on a Mac?
// plain

The `tar` command line is used to combine multiple files into a single file, or to extract files from a single file. It is a useful tool for archiving and transferring files.

To use the `tar` command line on a Mac, open your terminal and type the following command:

```
tar -cvf archive.tar file1 file2
```

This command will create an archive file called `archive.tar` which contains `file1` and `file2`.

To extract files from `archive.tar`, use the following command:

```
tar -xvf archive.tar
```

This command will extract the contents of `archive.tar` into the current directory.

## Code explanation


* `tar`: The tar command line tool
* `-cvf`: The flags used to create the archive file
* `-xvf`: The flags used to extract the archive file
* `archive.tar`: The name of the archive file
* `file1` and `file2`: The files to be archived/extracted

For more information on the `tar` command line, see the following links:

* [tar man page](https://linux.die.net/man/1/tar)
* [tar command tutorial](https://www.computerhope.com/unix/utar.htm)

onelinerhub: [How do I use the tar command line on a Mac?](https://onelinerhub.com/cli-tar/how-do-i-use-the-tar-command-line-on-a-mac)