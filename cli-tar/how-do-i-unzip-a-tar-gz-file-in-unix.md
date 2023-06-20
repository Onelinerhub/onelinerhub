# How do I unzip a tar.gz file in Unix?
// plain

To unzip a tar.gz file in Unix, use the following command:

```tar -xzf <file_name>.tar.gz```

This command will extract the contents of the tar.gz file into the current directory.

The command parts are:

* `tar`: The tar command is used to create, modify, and extract tar archives.
* `-xzf`: This option tells tar to extract the contents of the tar.gz file.
  * `-x`: Extract files from an archive.
  * `-z`: Filter the archive through gzip.
  * `-f`: Use the following tar archive for the operation.
* `<file_name>.tar.gz`: The name of the tar.gz file to be extracted.

For more information, please refer to the following links:

* [GNU tar Manual](https://www.gnu.org/software/tar/manual/html_node/tar_45.html)
* [How to unzip a tar.gz file](https://www.cyberciti.biz/faq/how-to-unzip-a-tar-gz-file/)

onelinerhub: [How do I unzip a tar.gz file in Unix?](https://onelinerhub.com/cli-tar/how-do-i-unzip-a-tar-gz-file-in-unix)