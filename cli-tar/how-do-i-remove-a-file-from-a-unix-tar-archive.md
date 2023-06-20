# How do I remove a file from a Unix tar archive?
// plain

To remove a file from a Unix tar archive, you can use the `tar --delete` command. The syntax for this command is `tar --delete <archive> <filename>`. For example, to delete the file `file.txt` from the archive `archive.tar`, you would use:

```
tar --delete archive.tar file.txt
```

The command will delete the file from the archive and print a message like the following:

```
tar: Deleting file `file.txt' from archive `archive.tar'
```

The parts of the command are as follows:

- `tar`: The command to use for manipulating tar archives
- `--delete`: The flag to indicate that you want to delete a file from the archive
- `archive.tar`: The name of the tar archive
- `file.txt`: The name of the file to delete from the archive

For more information on the `tar --delete` command, see the manual page [here](https://linux.die.net/man/1/tar).

onelinerhub: [How do I remove a file from a Unix tar archive?](https://onelinerhub.com/cli-tar/how-do-i-remove-a-file-from-a-unix-tar-archive)