# How do I use Unix tar and zip to compress files?
// plain

Using `tar` and `zip` in Unix is a great way to compress files. Here is an example of how to use `tar` to compress a directory and all of its contents:

```
tar -zcvf compressed-directory.tar.gz directory-name
```

This command will create a file called `compressed-directory.tar.gz` that contains all of the contents of `directory-name`. The options used in the command are as follows:

* `-z`: Compress the archive using gzip
* `-c`: Create a new archive
* `-v`: Verbosely list files which are processed
* `-f`: Use archive file or device ARCHIVE

You can also use `zip` to compress files in Unix. Here is an example of how to use `zip` to compress a single file:

```
zip compressed-file.zip file-name
```

This command will create a file called `compressed-file.zip` that contains the contents of `file-name`.

For more information about using `tar` and `zip` in Unix, see the following links:

* [tar man page](http://man7.org/linux/man-pages/man1/tar.1.html)
* [zip man page](http://man7.org/linux/man-pages/man1/zip.1.html)

onelinerhub: [How do I use Unix tar and zip to compress files?](https://onelinerhub.com/cli-tar/how-do-i-use-unix-tar-and-zip-to-compress-files)