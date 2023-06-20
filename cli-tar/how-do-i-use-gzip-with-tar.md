# How do I use gzip with tar?
// plain

Using gzip with tar allows for the compression of multiple files into one file with the .tar.gz extension. This is done by using the `tar` command with the `-z` or `--gzip` flag.

For example, to compress the files `file1.txt` and `file2.txt` into a single file called `archive.tar.gz`, you would use the following command:

```
tar -czvf archive.tar.gz file1.txt file2.txt
```

The output of the above command should look something like this:

```
file1.txt
file2.txt
```

The command is made up of the following parts:

* `tar`: The command to create an archive.
* `-czvf`: Flags that mean to create an archive, compress it with gzip, verbosely list the files being archived, and save it to a file.
* `archive.tar.gz`: The name of the output file.
* `file1.txt` & `file2.txt`: The files to be archived.

For more information, please see the following resources:

* [tar documentation](https://www.gnu.org/software/tar/manual/tar.html)
* [gzip documentation](https://www.gnu.org/software/gzip/manual/gzip.html)

onelinerhub: [How do I use gzip with tar?](https://onelinerhub.com/cli-tar/how-do-i-use-gzip-with-tar)