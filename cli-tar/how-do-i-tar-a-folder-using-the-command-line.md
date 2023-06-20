# How do I tar a folder using the command line?
// plain

Tar is a command line utility used to create and manipulate archive files. To tar a folder using the command line, use the following command:

```
tar -czvf <name_of_archive_file>.tar.gz <name_of_folder>
```

This command will create a tar.gz archive file of the specified folder. The options used are:

* `-c`: Create an archive.
* `-z`: Compress the archive with gzip.
* `-v`: Verbosely list files which are processed.
* `-f`: Allows you to specify the filename of the archive.

For example, if you wanted to create an archive of the folder `my_folder` and name it `my_archive.tar.gz`, you would use the following command:

```
tar -czvf my_archive.tar.gz my_folder
```

The output of this command will be a list of the files which are being archived.

For more information on the tar command, see the [GNU Tar Manual](https://www.gnu.org/software/tar/manual/tar.html).

onelinerhub: [How do I tar a folder using the command line?](https://onelinerhub.com/cli-tar/how-do-i-tar-a-folder-using-the-command-line)