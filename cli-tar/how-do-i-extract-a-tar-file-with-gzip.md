# How do I extract a tar file with gzip?
// plain

To extract a tar file with gzip, you can use the following command:
```
tar -xzvf <file_name.tar.gz>
```
This command will extract the contents of the tar file into the current directory.

The parts of the command are:
- `tar` - the tar command
- `-xzvf` - flags to extract the tar file
- `<file_name.tar.gz>` - the name of the tar file you want to extract

The `-x` flag tells tar to extract the contents of the file. The `-z` flag tells tar to decompress the file using gzip. The `-v` flag tells tar to be verbose and display the progress of the extraction. The `-f` flag tells tar that you are giving it a file name.

After running the command, the contents of the tar file will be extracted into the current directory.

For more information, see the [tar command man page](https://linux.die.net/man/1/tar).

onelinerhub: [How do I extract a tar file with gzip?](https://onelinerhub.com/cli-tar/how-do-i-extract-a-tar-file-with-gzip)