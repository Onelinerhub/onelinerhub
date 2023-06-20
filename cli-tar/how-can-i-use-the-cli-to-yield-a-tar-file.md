# How can I use the CLI to yield a tar file?
// plain

The CLI (Command Line Interface) can be used to create a tar file, which is a type of archive file that contains multiple files and folders. To do this, the `tar` command must be used.

The following example code will create a tar file called `my_archive.tar` from the contents of the folder `my_folder`.

```
tar -cvf my_archive.tar my_folder/
```

This command has four parts:
* `tar`: the command to create a tar file
* `-cvf`: the options used to create the tar file
    * `-c`: create a new archive
    * `-v`: verbose output
    * `-f`: specify the filename for the archive
* `my_archive.tar`: the name of the tar file to be created
* `my_folder/`: the path to the folder to be archived

The output of this command will be a list of the files and folders that were archived, similar to the following:

```
my_folder/
my_folder/file1.txt
my_folder/file2.txt
my_folder/folder1/
my_folder/folder1/file3.txt
```

For more information, refer to the following links:

* [GNU tar manual](https://www.gnu.org/software/tar/manual/html_node/tar_6.html)
* [tar command tutorial](https://linuxize.com/post/how-to-create-tar-gz-file-in-linux/)

onelinerhub: [How can I use the CLI to yield a tar file?](https://onelinerhub.com/cli-tar/how-can-i-use-the-cli-to-yield-a-tar-file)