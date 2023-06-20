# How do I read a gzip tar.gz file?
// plain

To read a gzip tar.gz file, you first need to unpack it. This can be done using the `tar` command. The following command will unpack a gzip tar.gz file in the current directory:

```
tar -xzvf <filename>.tar.gz
```

This command will extract the contents of the file and create a directory with the same name as the file.

The parts of the command are as follows:
- `tar`: The command to unpack a tar file
- `-xzvf`: Flags for the command, they indicate what type of file it is and how to unpack it
- `<filename>.tar.gz`: The name of the file to be unpacked

Once the file is unpacked, the contents can be read using the appropriate command for the type of file. For example, if the tar file contains a text file, it can be read with the `cat` command:

```
cat <filename>.txt
```

This will print the contents of the file to the terminal.

## Helpful links
- [tar command](https://www.computerhope.com/unix/utar.htm)
- [gzip command](https://www.computerhope.com/unix/ugzip.htm)

onelinerhub: [How do I read a gzip tar.gz file?](https://onelinerhub.com/cli-tar/how-do-i-read-a-gzip-tar-gz-file)