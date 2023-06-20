# How do I create a tar.gz file using the command line?
// plain

Creating a tar.gz file using the command line is a simple process. The `tar` command can be used to create a tar file, and the `gzip` command can be used to compress the tar file. This can be done in one step with the `-z` flag.

The following example command creates a tar.gz file from the `my-directory` directory:

```
tar -zcvf my-directory.tar.gz my-directory
```

The `-z` flag tells `tar` to compress the tar file using `gzip`. The `-c` flag creates a new tar file, the `-v` flag enables verbose output, and the `-f` flag specifies the file name for the tar file.

The output of the command should look like this:

```
tar: Removing leading `/' from member names
my-directory/
my-directory/file1.txt
my-directory/file2.txt
my-directory/file3.txt
```

The `my-directory.tar.gz` file will now be created in the current directory.

Parts of the command:
- `tar`: The command used to create tar files
- `-z`: Flag to tell `tar` to compress the tar file using `gzip`
- `-c`: Flag to create a new tar file
- `-v`: Flag to enable verbose output
- `-f`: Flag to specify the file name for the tar file

## Helpful links
- [GNU Tar Manual](https://www.gnu.org/software/tar/manual/html_node/tar_45.html)
- [Gzip Manual](https://www.gnu.org/software/gzip/manual/gzip.html)

onelinerhub: [How do I create a tar.gz file using the command line?](https://onelinerhub.com/cli-tar/how-do-i-create-a-tar-gz-file-using-the-command-line)