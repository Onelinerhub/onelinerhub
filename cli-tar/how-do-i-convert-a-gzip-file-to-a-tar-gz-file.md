# How do I convert a gzip file to a tar.gz file?
// plain

To convert a gzip file to a tar.gz file, you can use the `tar` command. The command will create a tar archive with the given gzip file.

For example, if you have a gzip file named `myfile.gz`, you can use the following command to convert it to a tar.gz file:

```
tar -zcvf myfile.tar.gz myfile.gz
```

The command will create a tar.gz file named `myfile.tar.gz` with the contents of `myfile.gz`.

The command consists of the following parts:

* `tar`: The command for creating a tar archive
* `-zcvf`: The flags for creating a gzip-compressed tar archive
* `myfile.tar.gz`: The name of the tar.gz file to be created
* `myfile.gz`: The name of the gzip file to be converted

For more information, see the [tar command man page](https://linux.die.net/man/1/tar).

onelinerhub: [How do I convert a gzip file to a tar.gz file?](https://onelinerhub.com/cli-tar/how-do-i-convert-a-gzip-file-to-a-tar-gz-file)