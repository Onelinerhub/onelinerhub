# How can I use a single command to tar and gzip a file?
// plain

The command `tar -czf <name_of_archive>.tar.gz <name_of_file_or_directory>` can be used to tar and gzip a file or directory. This command will create a tarball (a single file) containing the file or directory and its contents.

For example, the following command will create an archive called `example.tar.gz` containing the file `example.txt`:
```
tar -czf example.tar.gz example.txt
```
The command will produce no output.

The parts of the command are as follows:
- `tar`: The tar command is used to create, modify, and extract files from archives.
- `-czf`: These are flags that tell tar to create an archive (`-c`), compress it using gzip (`-z`), and use the specified file name for the archive (`-f`).
- `example.tar.gz`: This is the name of the archive that will be created.
- `example.txt`: This is the name of the file or directory that will be compressed and added to the archive.

For more information, see [the tar man page](https://linux.die.net/man/1/tar) or [this tutorial](https://www.linode.com/docs/tools-reference/linux-commands/tar-create-and-unpack-tar-gz-files/).

onelinerhub: [How can I use a single command to tar and gzip a file?](https://onelinerhub.com/cli-tar/how-can-i-use-a-single-command-to-tar-and-gzip-a-file)