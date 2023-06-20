# How do I compress a file with Unix tar gz?
// plain

Compressing a file with Unix tar gz is a simple process. To do this, you will need to use the tar command. The tar command allows you to create an archive of multiple files or directories.

To compress a file with tar gz, you will need to use the following command:
```
tar -czvf filename.tar.gz /path/to/file
```

The command will create an archive of the file located in the provided path and save it as `filename.tar.gz` in the current directory. The `-c` flag indicates that the tar command should create an archive, the `-z` flag indicates that you want to compress the file with gzip, the `-v` flag will provide verbose output, and the `-f` flag indicates the name and location of the archive.

The following is an example of the output you can expect from the command:
```
adding: path/to/file (deflated 86%)
```

The output indicates that the file has been added to the archive and compressed with gzip.

The parts of the command are as follows:
- `tar`: The command to create an archive.
- `-c`: Flag to indicate that an archive should be created.
- `-z`: Flag to indicate that the file should be compressed with gzip.
- `-v`: Flag to provide verbose output.
- `-f`: Flag to indicate the name and location of the archive.
- `filename.tar.gz`: The name and location of the archive.
- `/path/to/file`: The path to the file that should be added to the archive.

For more information about the tar command, see the [GNU tar manual](https://www.gnu.org/software/tar/manual/html_node/tar_7.html).

onelinerhub: [How do I compress a file with Unix tar gz?](https://onelinerhub.com/cli-tar/how-do-i-compress-a-file-with-unix-tar-gz)