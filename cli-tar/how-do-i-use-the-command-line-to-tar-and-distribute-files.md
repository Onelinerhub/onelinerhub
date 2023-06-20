# How do I use the command line to tar and distribute files?
// plain

The command line utility `tar` is used to create, modify, and extract files from an archive. To tar and distribute files, you need to use the following command:

```
tar -cvf <archive_name>.tar <file_name>
```

This command will create a tar archive with the name `<archive_name>.tar` containing the file `<file_name>`. To distribute the tar archive, you can use a file transfer protocol like `scp`:

```
scp <archive_name>.tar <user>@<host>:<destination_path>
```

This command will copy the tar archive to the remote host specified by `<user>@<host>` and place it in the `<destination_path>`.

Parts of the command:
- `tar`: A command line utility used for creating, modifying, and extracting files from an archive.
- `-cvf`: Options for the `tar` command. `-c` creates a new archive, `-v` displays the progress of the archive creation, and `-f` specifies the name of the archive.
- `<archive_name>.tar`: The name of the tar archive to be created.
- `<file_name>`: The name of the file to be added to the archive.
- `scp`: A command line utility used to securely copy files between hosts.
- `<user>@<host>`: The remote host to which the tar archive should be copied.
- `<destination_path>`: The path on the remote host where the tar archive should be placed.

## Helpful links
- [tar man page](https://linux.die.net/man/1/tar)
- [scp man page](https://linux.die.net/man/1/scp)

onelinerhub: [How do I use the command line to tar and distribute files?](https://onelinerhub.com/cli-tar/how-do-i-use-the-command-line-to-tar-and-distribute-files)