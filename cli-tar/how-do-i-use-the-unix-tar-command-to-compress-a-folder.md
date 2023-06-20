# How do I use the Unix tar command to compress a folder?
// plain

The Unix tar command is used to compress a folder by creating a tarball (a tar archive file). To use the tar command, open the command line and type:

```
tar -cvf <filename>.tar <foldername>
```

This command will create a tar archive file named <filename>.tar containing the contents of the <foldername> folder.

The parts of the command are as follows:

* `tar` - the command to create an archive
* `-cvf` - the flags used to create the archive
  * `-c` - create a new archive
  * `-v` - verbose output (optional)
  * `-f` - specify the filename of the archive
* `<filename>.tar` - the name of the archive to be created
* `<foldername>` - the name of the folder to be compressed

To extract the contents of the archive, use the following command:

```
tar -xvf <filename>.tar
```

This command will extract the contents of the <filename>.tar archive into the current working directory.

## Helpful links

* [Tar command man page](https://linux.die.net/man/1/tar)
* [How to Use Tar Command in Linux](https://www.linode.com/docs/tools-reference/tools/how-to-use-tar-command-in-linux/)

onelinerhub: [How do I use the Unix tar command to compress a folder?](https://onelinerhub.com/cli-tar/how-do-i-use-the-unix-tar-command-to-compress-a-folder)