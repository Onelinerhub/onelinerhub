# How do I use the command line to tar and zip a file?
// plain

The command line is a powerful tool for managing files and directories. To tar and zip a file, you can use the `tar` and `gzip` commands.

The `tar` command is used to create a tarball, which is a single file containing multiple files and directories. The `gzip` command is used to compress the tarball, reducing its size.

Here's an example of how to tar and zip a file using the command line:

```
$ tar -cvf myfile.tar myfile.txt
$ gzip myfile.tar
```

The `-cvf` option tells `tar` to create a tarball with verbose output. The `gzip` command will compress the tarball, creating a new file called `myfile.tar.gz`.

The parts of the command are:

* `tar`: the command to create a tarball
* `-cvf`: the options to create a tarball with verbose output
* `myfile.tar`: the name of the tarball to create
* `myfile.txt`: the file to be included in the tarball
* `gzip`: the command to compress the tarball
* `myfile.tar.gz`: the name of the compressed tarball

For more information on using the `tar` and `gzip` commands, see the [GNU tar manual](https://www.gnu.org/software/tar/manual/tar.html) and the [gzip manual](https://www.gnu.org/software/gzip/manual/gzip.html).

onelinerhub: [How do I use the command line to tar and zip a file?](https://onelinerhub.com/cli-tar/how-do-i-use-the-command-line-to-tar-and-zip-a-file)