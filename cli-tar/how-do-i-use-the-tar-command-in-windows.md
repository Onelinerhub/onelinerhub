# How do I use the tar command in Windows?
// plain

The `tar` command can be used in Windows to create, modify, and extract files from an archive. To use the `tar` command in Windows, you will need to install the [GNU Tar for Windows](https://www.gnu.org/software/tar/).

Once you have installed `GNU Tar`, you can use the `tar` command from the command line. For example, the following command will create an archive of a file called `example.txt`:

```
tar -cvf example.tar example.txt
```

The command options are as follows:

* `-c`: Create an archive
* `-v`: Verbose output
* `-f`: Name of the archive

The output of the command will be the name of the archive created, in this case `example.tar`.

To extract the contents of the archive, use the `-x` option instead:

```
tar -xvf example.tar
```

The output of this command will be the contents of the archive.

For more information on using `tar` in Windows, see the [GNU Tar documentation](https://www.gnu.org/software/tar/manual/html_node/tar_45.html).

onelinerhub: [How do I use the tar command in Windows?](https://onelinerhub.com/cli-tar/how-do-i-use-the-tar-command-in-windows)