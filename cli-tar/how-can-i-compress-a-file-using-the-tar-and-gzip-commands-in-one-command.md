# How can I compress a file using the tar and gzip commands in one command?
// plain

To compress a file using the tar and gzip commands in one command, you can use the following command:

```
tar -czvf <output-filename.tar.gz> <input-filename>
```

This command will create an output file with the name `<output-filename.tar.gz>` containing the contents of the input file `<input-filename>`.

The command parts are:
- `tar`: the tar command is used to create an archive file
- `-czvf`: this is a combination of flags used to create a gzip compressed tar archive
- `<output-filename.tar.gz>`: this is the name of the output file to be created
- `<input-filename>`: this is the name of the input file to be compressed

For more information about the tar command, you can refer to the following links:
- [GNU Tar Manual](https://www.gnu.org/software/tar/manual/tar.html)
- [LinuxCommand.org Tar Command Tutorial](http://www.linuxcommand.org/man_pages/tar1.html)

onelinerhub: [How can I compress a file using the tar and gzip commands in one command?](https://onelinerhub.com/cli-tar/how-can-i-compress-a-file-using-the-tar-and-gzip-commands-in-one-command)