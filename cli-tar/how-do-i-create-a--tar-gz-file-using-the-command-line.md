# How do I create a .tar.gz file using the command line?
// plain

Creating a `.tar.gz` file using the command line is a two-step process. First, you must create a `.tar` file, and then compress the `.tar` file into a `.tar.gz` file.

To create a `.tar` file, use the command `tar -cvf filename.tar file1 file2 file3`:

```
$ tar -cvf myfiles.tar file1 file2 file3
file1
file2
file3
```

This command will create a `.tar` file named `myfiles.tar` containing the files `file1`, `file2`, and `file3`.

To compress the `.tar` file into a `.tar.gz` file, use the command `gzip filename.tar`:

```
$ gzip myfiles.tar
```

This will create a `.tar.gz` file named `myfiles.tar.gz`.

## Code explanation
**

* `tar -cvf filename.tar file1 file2 file3`: Creates a `.tar` file named `filename.tar` containing the files `file1`, `file2`, and `file3`.
* `gzip filename.tar`: Compresses the `.tar` file into a `.tar.gz` file named `filename.tar.gz`.

**## Helpful links**

* [Tutorial on Creating tar Files](https://www.cyberciti.biz/faq/howto-linux-unix-create-tar-file/)
* [Tutorial on Compressing tar Files](https://www.cyberciti.biz/faq/howto-linux-unix-compress-tar-file/)

onelinerhub: [How do I create a .tar.gz file using the command line?](https://onelinerhub.com/cli-tar/how-do-i-create-a--tar-gz-file-using-the-command-line)