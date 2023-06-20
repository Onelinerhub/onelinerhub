# How do I create a tar.zip file in Unix?
// plain

Creating a tar.zip file in Unix is a two-step process that involves compressing the files with tar and then compressing the tar archive with gzip.

To create a tar.zip file, run the following command in the terminal:

```
tar -czvf <file_name>.tar.gz <directory_name>
```

This command will create a tar archive of the specified directory and then compress it with gzip.

The command has four parts:
1. `tar`: The command to create an archive.
2. `-czvf`: Flags to tell tar to compress the archive with gzip and to create a file.
3. `<file_name>.tar.gz`: The name of the archive file.
4. `<directory_name>`: The directory to be archived.

For example, to create a tar.zip file of the `my_directory` directory, run

```
tar -czvf my_archive.tar.gz my_directory
```

This will create a file called `my_archive.tar.gz` containing the contents of the `my_directory` directory.

## Helpful links
- [tar command](https://www.computerhope.com/unix/utar.htm)
- [gzip command](https://www.computerhope.com/unix/ugzip.htm)

onelinerhub: [How do I create a tar.zip file in Unix?](https://onelinerhub.com/cli-tar/how-do-i-create-a-tar-zip-file-in-unix)