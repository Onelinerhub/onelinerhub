# How do I remove a file from a Unix tar archive?
// plain

To remove a file from a Unix tar archive, use the `tar` command with the `--delete` option.

For example, to remove `file.txt` from the archive `archive.tar`, run the following command:

```
tar --delete -f archive.tar file.txt
```

The command will delete `file.txt` from the archive without extracting it.

The command consists of the following parts:

* `tar` - the command to manipulate tar archives
* `--delete` - the option to delete a file from the archive
* `-f` - the option to specify the archive file
* `archive.tar` - the tar archive from which the file will be deleted
* `file.txt` - the file to be deleted from the archive

For more information, see the [GNU tar manual](https://www.gnu.org/software/tar/manual/tar.html#Deleting).

onelinerhub: [How do I remove a file from a Unix tar archive?](https://onelinerhub.com/cli-tar/how-do-i-remove-a-file-from-a-unix-tar-archive-1687286498)