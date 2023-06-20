# How do I use the tar command in Windows command line?
// plain

The `tar` command is a useful tool for archiving files and directories in Windows command line. It is available as part of the [GNUWin32 project](http://gnuwin32.sourceforge.net/packages/gtar.htm), which provides a port of many GNU utilities for Windows.

To use `tar` in the Windows command line, the `tar.exe` executable must be added to the system PATH. Once the executable is added to the PATH, `tar` can be used by typing `tar` followed by the options and arguments.

For example, to create an archive of the `C:\mydir` directory, the following command can be used:

```
tar -cf mydir.tar C:\mydir
```

This will create a tar archive named `mydir.tar` in the current directory.

To extract the contents of an archive, the `-x` option can be used, as in:

```
tar -xf mydir.tar
```

This will extract the contents of `mydir.tar` into the current directory.

Other useful options include `-z` to compress the archive with `gzip`, `-j` to compress the archive with `bzip2`, and `-v` to list the files as they are added or extracted from the archive.

For more information about the `tar` command, see the [GNU tar manual](https://www.gnu.org/software/tar/manual/tar.html).

onelinerhub: [How do I use the tar command in Windows command line?](https://onelinerhub.com/cli-tar/how-do-i-use-the-tar-command-in-windows-command-line)