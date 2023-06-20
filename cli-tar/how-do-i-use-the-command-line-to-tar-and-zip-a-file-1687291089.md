# How do I use the command line to tar and zip a file?
// plain

The command line can be used to tar and zip a file using the `tar` and `gzip` commands.

`tar` is used to create an archive of multiple files into a single file, while `gzip` is used to compress a single file.

For example, to tar and zip a file called `myfile.txt`, the following command can be used:

```
tar -czvf myfile.tar.gz myfile.txt
```

This command will create a tarball archive called `myfile.tar.gz` which contains the file `myfile.txt` and compress it using gzip.

The parts of the command are as follows:

- `tar`: the tar command
- `-czvf`: flags that specify the action to be taken, in this case `c` for create, `z` for gzip, `v` for verbose, and `f` for file
- `myfile.tar.gz`: the name of the tarball archive to be created
- `myfile.txt`: the file to be archived and compressed

For more information, see the following links:

- [GNU Tar Manual](https://www.gnu.org/software/tar/manual/tar.html)
- [Gzip Manual](https://www.gnu.org/software/gzip/manual/gzip.html)

onelinerhub: [How do I use the command line to tar and zip a file?](https://onelinerhub.com/cli-tar/how-do-i-use-the-command-line-to-tar-and-zip-a-file-1687291089)