# How do I use the command line to create a backup tar file?
// plain

To create a backup tar file using the command line, you can use the `tar` command. The basic syntax is `tar -czf <filename>.tar.gz <source_directory>`. This will create a compressed tar file from the source directory.

For example, to create a tar file from the directory `/home/user/Documents` with the filename `backup.tar.gz`, you can use the command:
```
tar -czf backup.tar.gz /home/user/Documents
```

The parts of the command are:
- `tar`: the tar command
- `-czf`: flags to set the compression level, create a tar file, and specify the filename
- `backup.tar.gz`: the filename of the tar file to be created
- `/home/user/Documents`: the source directory to be backed up

If the command is successful, no output will be shown. To verify that the tar file was created, you can use the `ls` command to list the files in the directory.

For more information about the `tar` command, you can refer to the [GNU tar manual](https://www.gnu.org/software/tar/manual/html_node/tar_6.html).

onelinerhub: [How do I use the command line to create a backup tar file?](https://onelinerhub.com/cli-tar/how-do-i-use-the-command-line-to-create-a-backup-tar-file)