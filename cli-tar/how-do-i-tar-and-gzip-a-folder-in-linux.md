# How do I tar and gzip a folder in Linux?
// plain

The `tar` command is a great way to compress a folder in Linux. It creates a single file that contains all of the files and folders inside the folder you specified. To tar and gzip a folder in Linux, you can use the following command:

```
tar -zcvf <filename>.tar.gz <folder_name>
```

This will create a `<filename>.tar.gz` file that contains the contents of the `<folder_name>`.

The parts of the command are as follows:

* `tar`: The command to create the archive
* `-zcvf`: The flags used to create a gzipped tar archive
* `<filename>.tar.gz`: The name of the archive file to be created
* `<folder_name>`: The name of the folder to be compressed

For more information, see the [GNU tar documentation](https://www.gnu.org/software/tar/manual/html_node/tar_5.html).

onelinerhub: [How do I tar and gzip a folder in Linux?](https://onelinerhub.com/cli-tar/how-do-i-tar-and-gzip-a-folder-in-linux)