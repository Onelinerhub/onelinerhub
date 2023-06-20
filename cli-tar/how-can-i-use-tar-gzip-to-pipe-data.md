# How can I use tar gzip to pipe data?
// plain

Tar gzip is a powerful tool for compressing and archiving data. It can be used to pipe data from one process to another in order to save disk space and reduce transfer time. The following example shows how to use tar gzip to pipe data from a source file to a destination file:

```
tar czf - source_file | (cd destination_directory; tar xzf -)
```

This command will create a tar archive of the source file and pipe it to the destination directory, where it will be extracted.

The command is composed of two parts:

1. `tar czf - source_file`: This part creates a tar archive of the source file and sends it to the standard output.

2. `(cd destination_directory; tar xzf -)`: This part changes the working directory to the destination directory and extracts the tar archive from the standard input.

For more information on tar gzip, please refer to the [GNU tar documentation](https://www.gnu.org/software/tar/manual/html_node/tar_45.html).

onelinerhub: [How can I use tar gzip to pipe data?](https://onelinerhub.com/cli-tar/how-can-i-use-tar-gzip-to-pipe-data)