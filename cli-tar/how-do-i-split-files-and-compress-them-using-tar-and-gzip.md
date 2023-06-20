# How do I split files and compress them using tar and gzip?
// plain

To split files and compress them using tar and gzip, you can use the following command:

```
tar -czvf <name_of_tar_file>.tar.gz <name_of_file_to_compress>
```

This command will create a `<name_of_tar_file>.tar.gz` file which contains the compressed version of `<name_of_file_to_compress>`.

## Code explanation


- `tar` - This is the command to create a tar file.
- `-czvf` - This is the set of flags for the command. `-c` is for creating a new tar file, `-z` is for compressing the file using gzip, `-v` is for verbose output and `-f` is for the file name of the tar file.
- `<name_of_tar_file>.tar.gz` - This is the name of the tar file that will be created.
- `<name_of_file_to_compress>` - This is the name of the file that will be compressed and added to the tar file.

## Helpful links

- [Tar Command Tutorial](https://www.guru99.com/tar-command-in-linux-unix.html)
- [Gzip Command Tutorial](https://www.tecmint.com/gzip-and-gunzip-command-in-linux/)

onelinerhub: [How do I split files and compress them using tar and gzip?](https://onelinerhub.com/cli-tar/how-do-i-split-files-and-compress-them-using-tar-and-gzip)