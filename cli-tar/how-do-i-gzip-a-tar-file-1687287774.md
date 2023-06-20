# How do I gzip a tar file?
// plain

To gzip a tar file, you can use the `tar` command in combination with the `gzip` command. The syntax for this is:

```
tar -zcvf <output_file_name>.tar.gz <input_file_name>
```

This will create a gzipped tar file named `<output_file_name>.tar.gz` containing the `<input_file_name>`.

## Code explanation


- `tar`: the tar command used to create a tar file
- `-zcvf`: the flags used to indicate gzip compression and create a tar archive
- `<output_file_name>.tar.gz`: the name of the output file
- `<input_file_name>`: the name of the input file

## Helpful links

- [Tar Command](https://www.computerhope.com/unix/utar.htm)
- [Gzip Command](https://www.computerhope.com/unix/ugzip.htm)

onelinerhub: [How do I gzip a tar file?](https://onelinerhub.com/cli-tar/how-do-i-gzip-a-tar-file-1687287774)