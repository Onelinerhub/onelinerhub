# How do I use the tar command line options?
// plain

The `tar` command is a Unix-based utility for archiving files and directories. It is commonly used for creating backups, compressing files, and transferring data over the network.

The `tar` command uses the following syntax:

```
tar [options] <source> <destination>
```

The following options are available when using the `tar` command:

- `-c`: Create a new archive
- `-x`: Extract files from an existing archive
- `-t`: List the contents of an existing archive
- `-v`: Display verbose output
- `-f`: Specify the name of the archive file

For example, to create a new archive named `myarchive.tar` from the directory `/home/user/mydir`, you would use the following command:

```
tar -cvf myarchive.tar /home/user/mydir
```

This command will create a new archive named `myarchive.tar` in the current working directory.

To extract the contents of `myarchive.tar` into the current working directory, you would use the following command:

```
tar -xvf myarchive.tar
```

This command will extract the contents of `myarchive.tar` into the current working directory.

To list the contents of `myarchive.tar`, you would use the following command:

```
tar -tvf myarchive.tar
```

This command will list the contents of `myarchive.tar` in the current working directory.

For more information on the `tar` command and its options, see the following links:

- [GNU Tar Manual](https://www.gnu.org/software/tar/manual/tar.html)
- [Linux man page for tar](http://man7.org/linux/man-pages/man1/tar.1.html)

onelinerhub: [How do I use the tar command line options?](https://onelinerhub.com/cli-tar/how-do-i-use-the-tar-command-line-options)