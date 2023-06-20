# How can I use the CLI tar yarn command to compress files?
// plain

The `tar yarn` command is a command-line tool that can be used to compress files. It takes two arguments: the source file or directory and the destination file or directory.

For example, to compress a file called `example.txt` into a file called `example.tar.gz`, you can use the following command:
```
tar -zcf example.tar.gz example.txt
```

The `-z` flag tells tar to compress the file using gzip. The `-c` flag tells tar to create a new archive. The `-f` flag tells tar to use the specified file as the output archive.

You can also use the `tar yarn` command to compress an entire directory. For example, to compress a directory called `my_files` into a file called `my_files.tar.gz`, you can use the following command:
```
tar -zcf my_files.tar.gz my_files
```

The output of the command will be a compressed file containing all the files in the `my_files` directory.

## Helpful links
- [GNU Tar Manual](https://www.gnu.org/software/tar/manual/tar.html)
- [Tar Command Tutorial](https://linuxize.com/post/how-to-use-tar-command-in-linux/)

onelinerhub: [How can I use the CLI tar yarn command to compress files?](https://onelinerhub.com/cli-tar/how-can-i-use-the-cli-tar-yarn-command-to-compress-files)