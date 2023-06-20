# How do I use the tar command line tool on Linux?
// plain

The `tar` command line tool on Linux is used to create, extract, and manipulate files that are archived in the tar format.

The basic syntax for the `tar` command is: `tar [options] [archive] [files]`.

Here is an example of how to use the `tar` command to create an archive:

```
tar -cvf archive.tar file1 file2
```

This command will create an archive named `archive.tar` containing the files `file1` and `file2`.

To extract files from an archive, use the `-x` option, like this:

```
tar -xvf archive.tar
```

This command will extract the contents of `archive.tar` into the current directory.

The `tar` command also has options to add files to an existing archive, list the contents of an archive, and more. For more information, see the man page for `tar` or the following links:

* [GNU tar Manual](https://www.gnu.org/software/tar/manual/tar.html)
* [Linux man page for tar](http://man7.org/linux/man-pages/man1/tar.1.html)

onelinerhub: [How do I use the tar command line tool on Linux?](https://onelinerhub.com/cli-tar/how-do-i-use-the-tar-command-line-tool-on-linux)