# How can I use shell jalan tar to create a compressed file?
// plain

Shell jalan tar is a command line utility used to create, modify, and extract files from an archive. It can be used to create a compressed file by using the following command:

```
tar -czvf <filename>.tar.gz <file or directory to compress>
```

This command will create a compressed file with the extension `.tar.gz` from the specified file or directory.

The command consists of the following parts:

1. `tar` – This specifies the tar command.
2. `-czvf` – This specifies the options used to create the compressed file. The options used are:
    - c – Create a new archive.
    - z – Compress the archive using gzip.
    - v – Verbosely list files processed.
    - f – Use the archive file specified.
3. `<filename>.tar.gz` – This is the name of the compressed file to be created.
4. `<file or directory to compress>` – This is the name of the file or directory to be compressed.

The output of the command will be the name of the file or directory being compressed.

## Helpful links
- [GNU Tar Manual](https://www.gnu.org/software/tar/manual/html_node/tar_45.html)
- [Linux Command Line Cheat Sheet](https://www.linuxtrainingacademy.com/linux-command-line-cheat-sheet/)

onelinerhub: [How can I use shell jalan tar to create a compressed file?](https://onelinerhub.com/cli-tar/how-can-i-use-shell-jalan-tar-to-create-a-compressed-file)