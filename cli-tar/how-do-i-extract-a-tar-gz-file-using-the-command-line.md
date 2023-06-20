# How do I extract a tar.gz file using the command line?
// plain

To extract a tar.gz file using the command line, use the following syntax:
```
tar -xzvf <filename>.tar.gz
```

The parts of the code are as follows:
- `tar`: the command to extract files
- `-xzvf`: the options for the command, which stands for "extract, gzip, verbose, file"
- `<filename>.tar.gz`: the name of the file to be extracted

The output of the command should look something like this:
```
x file_1.txt
x file_2.txt
x file_3.txt
```

This shows the command successfully extracting the files in the tar.gz archive.

## Helpful links
- [GNU Tar Manual](https://www.gnu.org/software/tar/manual/html_node/tar_49.html)
- [How To Extract Tar.gz Files Using Linux Command Line](https://www.linuxtechi.com/extract-tar-gz-files-using-linux-command-line/)

onelinerhub: [How do I extract a tar.gz file using the command line?](https://onelinerhub.com/cli-tar/how-do-i-extract-a-tar-gz-file-using-the-command-line)