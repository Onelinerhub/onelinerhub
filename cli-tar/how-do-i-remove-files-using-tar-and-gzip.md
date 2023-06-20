# How do I remove files using tar and gzip?
// plain

Using tar and gzip, you can remove files from an archive. The syntax to do so is `tar -zvf <archive name> --delete <files to delete>`. Here is an example:

```
tar -zvf archive.tar.gz --delete file1.txt
```

This command will delete the file `file1.txt` from the archive `archive.tar.gz`.

The parts of the command are as follows:
- `tar`: the tar command
- `-zvf`: tells tar to work with gzip-compressed archives
- `archive.tar.gz`: the name of the archive
- `--delete`: tells tar to delete the specified files
- `file1.txt`: the name of the file to delete

For more information, please see the following links:
- [tar man page](https://linux.die.net/man/1/tar)
- [gzip man page](https://linux.die.net/man/1/gzip)

onelinerhub: [How do I remove files using tar and gzip?](https://onelinerhub.com/cli-tar/how-do-i-remove-files-using-tar-and-gzip)