# How do I compress a file using the Unix tar command?
// plain

The Unix tar command allows you to compress a file. The following example shows how to compress a file named `file.txt`:

```
tar -czvf file.tar.gz file.txt
```

This command creates a compressed file named `file.tar.gz`. The options used in this command are:

- `-c`: This option creates a new tar archive.
- `-z`: This option compresses the tar archive with gzip.
- `-v`: This option prints the progress of the compression to the terminal.
- `-f`: This option tells tar to read or create the archive specified by the file name.

The output of the command should look like this:

```
file.txt
```

For more information about the tar command, please see the following links:

- [GNU Tar Manual](https://www.gnu.org/software/tar/manual/tar.html)
- [How to use Tar Command in Linux](https://www.linuxtechi.com/use-tar-command-linux-unix/)

onelinerhub: [How do I compress a file using the Unix tar command?](https://onelinerhub.com/cli-tar/how-do-i-compress-a-file-using-the-unix-tar-command)